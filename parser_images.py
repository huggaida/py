import requests, os

# url = 'https://cdn.wallpaper.com/main/styles/fp_480x294/s3/2019/05/frieze-new-york-2019-victoria-miro-p.jpg'
# r = requests.get(url, stream = True)
# with open ('1.jpg', 'bw' ) as f:
#     for chunk in r.iter_content(18192):
#         f.write(chunk)


urls = [
    'https://www.hdwallpapers.in/walls/messier_106_spiral_galaxy_5k-wide.jpg',
    'https://www.hdwallpapers.in/walls/helix_nebula_5k-wide.jpg',
    'https://www.hdwallpapers.in/walls/orion_nebula_hubble_space_telescope_5k-wide.jpg',
    'https://www.hdwallpapers.in/walls/solar_space-wide.jpg'
]
 
 
def get_file(url):
    r = requests.get(url, stream=True)
    return r
 
 
def get_name(url):
    name = url.split('/')[-1]
    folder = name.split('.')[0]
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.abspath(folder)
    return path + '/' + name
 
 
def save_image(name, file_object):
    with open(name, 'bw') as f:
        for chunk in file_object.iter_content(18192):
            f.write(chunk)
 
def main():
    for url in urls:
        save_image(get_name(url), get_file(url))
 
if __name__ == '__main__':
    main()
