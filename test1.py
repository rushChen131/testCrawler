class ImagedownPipeline(object):
    def process_item(self, item, spider):
        if 'image_url' in item:
            #images = []
            dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)

#            if not os.path.exists(dir_path):
#                os.makedirs(dir_path)
            for image_url in item['image_url']:
                image_page = item['image_page']
                dir_path = '%s/%s' %(dir_path, image_page)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

                us = image_url.split('/')[3:]
                image_file_name = '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                #images.append(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content():
                        #if not block:
                         #   break
                        handle.write(block)

            #item['images'] = images
        return item