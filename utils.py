import pandas as pd
import requests
import io
import random
import os
from dotenv import load_dotenv
from PIL import Image


def download_image(url):
    response = requests.get(url)
    return response.content

def save_image(content, file_name):
    with open(file_name, 'wb') as f:
        f.write(content)

def pad_image(img_path, color=(255, 255, 255)):
    im = Image.open(img_path)
    width, height = im.size
    if width == height: 
        return im
    max_dim = max(width, height)
    pad_img = Image.new(im.mode, (max_dim, max_dim), color)
    pad_img.paste(im, ((max_dim - width) // 2, (max_dim - height) // 2))
    return pad_img

def download_data_export(filename = "cleaned_export.csv"):
    """
    Downloads data from a specified url using credentials from environment variables.
    Removes testing rows and duplicates, fills in missing labels, and removes rows with no image.
    Saves the resulting dataframe to a csv file with the specified filename.

    Args:
        filename (str): The name of the file to save the cleaned dataframe to.

    Returns:
        tuple: A tuple containing a boolean indicating whether the dataframe is empty and the cleaned dataframe.
    """

    load_dotenv()
   
    url =  os.getenv("db_export_url")
    username = os.getenv("db_export_username")
    password =  os.getenv("db_export_password")

    r = requests.get(url, auth=(username, password))
    data = r.content
    df = pd.read_csv(io.StringIO(data.decode('utf-8')))

    # Remove unnecessary testing rows
    unnecessary_titles = ["test", "debug", "phil", "owner"]
    df = df[~df["title"].str.lower().str.contains("|".join(unnecessary_titles))]
    df = df[df['specimenId'].notna()]
    df = df[~df['specimenId'].str.isnumeric()]    
    df = df[~df["specimenId"].str.lower().str.contains("|".join(unnecessary_titles))]

    # morphSpecies is the true label provided by VCOs
    # if it is not filled in, use app predicted "species" column
    df['morphSpecies'] = df['morphSpecies'].fillna(df['species'])
    df['morphSex'] = df['morphSex'].fillna(df['sex'])

    # Remove rows with no image
    df = df[df["specimenId"].notna() & df["image"].notna()].copy()
    df.reset_index(drop=True, inplace=True)
    df['specimenId_unique']=df['title'] + "&&" + df['date'].str.replace('/', '-') + "&&" + df['specimenId']
    df['specimenId_unique'] = df['specimenId_unique'].str.replace(' ', '')
    df['specimenId'] = df['specimenId'].str.replace(' ', '')

    # Remove duplicate rows
    df.drop_duplicates(subset='specimenId_unique', keep='last', inplace=True)

    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} rows to {filename}")
    
    if len(df) == 0:
        return False, None
    else:
        return True, df

def pad(im, color):
    """
    Pads the image to make it a square"
    : im: image to pad
    : color: color to pad the image
    : returns padded image
    """
    # global pad_img
    width, height = im.size

    # if widht and height are same, padding is not required.
    if width == height:
        return im
    
    elif width > height:
        pad_img = Image.new(im.mode, (width, width), color)
        pad_img.paste(im, (0, (width - height) // 2))
    
    else:
        pad_img = Image.new(im.mode, (height, height), color)
        pad_img.paste(im, ((height - width)//2, 0))
    
    return pad_img

