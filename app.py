import spotipy
import urllib.request
import os
import math
from PIL import Image
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from time import sleep


def extract_id(url):
    #remove query from url -> '?" part'
    url_required_component = url.split('?',1)[0]

    #Get playlist id from the remaining url
    playlist_id = url_required_component.split('/')[-1]
    
    return playlist_id

def save_images(id):
    #Create environment variables or pass client id
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    pl_uri = 'spotify:playlist:' + id

    pl_offset = 0

    image_index = 0

    try:
         #make the temporary images directory
        os.mkdir(os.getcwd() + '/images')

        while True:
            results = spotify.playlist_tracks(pl_uri,
                                                offset=pl_offset,
                                                fields='items.track.id,items.track.album',
                                                limit=50,
                                                additional_types=['track'])

            if len(results['items']) != 0:
                for result in results['items']:
                    image_url = result['track']['album']['images'][0]['url']
                    resource = urllib.request.urlopen(image_url)
                    # image_path = 'images\image' + image_index + '.jpg'
                    output = open(f'images/image{image_index}.jpg', 'wb')
                    output.write(resource.read())
                    output.close()
                    image_index+=1

                #increase offset
                pl_offset += 50
            else:
                break

        return image_index
    except:
        print("Error in downloading or saving images")



def cleanup(num_images):
    try:
         # later remove images stored once collage is made
        for i in range(0,num_images):
            os.remove(f'images\image{i}.jpg')

        os.rmdir('images')
    except:
        print('Error in cleanup')



def find_collage_size(num_images):
    i = j = math.ceil(math.sqrt(num_images))

    #try to reduce the dimensions closer to the actual number of images
    while True:
        if((i*j == num_images) or (i*(j-1) < num_images)):
            return (i,j)
        else:
            j -= 1


def create_collage(r, c, num_images, filePath, fileName):
    width = r*640
    height = c*640

    image_index = 0

    collage = Image.new('RGBA', (height, width), (255,255,255,255))
    stop_loop = False
    for i in range(0, height, 640):
        if(stop_loop):
            break
        for j in range(0, width, 640):
            if(stop_loop):
                break
            current_image = Image.open(f'images/image{image_index}.jpg')
            image_index += 1

            #check if more images available
            if(image_index >= num_images):
                stop_loop = True
            
            collage.paste(current_image, (i,j))

    collage.save(filePath + '/' +fileName + '.png')
    collage.show()

def collage(playlist_url, filePath, fileName):
    #Get playlist ID from URL
    id = extract_id(playlist_url)

    #Download the required images to the images folder
    num_images = save_images(id)

    #Calculate the dimensions of the final collage
    r,c = find_collage_size(num_images)

    #create the collage
    create_collage(r,c,num_images, filePath, fileName)

    #cleanup after collage created
    cleanup(num_images)

if __name__ == '__main__':
    playlist_URL = 'Put Your playlist URL here'
    collage(playlist_URL)