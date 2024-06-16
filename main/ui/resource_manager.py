import lvgl as lv
from common import fs_driver
from imagetools import get_png_info, open_png
import usys as sys
global_image_cache={}
global_font_cache={}
def singleton(cls):
    instance = None
    def getinstance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return getinstance
@singleton
class ResourceManager:
    def __init__(self):
        global_font_cache = {}
        self.global_raw_cache={}
        lv.init()
        fs_drv = lv.fs_drv_t()
        fs_driver.fs_register(fs_drv, 'Z')
        print("初始化文件系统Z:盘")
        decoder = lv.img.decoder_create()
        decoder.info_cb = get_png_info
        decoder.open_cb = open_png

    def load_raw(self,file):
        """
        用于lottie文件缓存
        :param file:
        :return:
        """
        if file in self.global_raw_cache:
            print("hit file from cache->%s" % (file))
            return self.global_raw_cache[file]
        with open(file, 'r') as f:
            print("loading file->%s" % (file))
            raw_data = f.read()
            self.global_raw_cache[file]=raw_data
        return raw_data

    def load_img(self, file,width=240,height=240):
        """
        只支持png格式图片
        :param file:
        :return:
        """
        global global_image_cache
        if file in global_image_cache:
            print("hit file from cache->%s" % (file))
            return global_image_cache[file]
        try:
            with open(file, 'rb') as f:
                data = f.read()
        except:
            print(f'Could not open {file}')
            sys.exit()
        print("loading png file:%s,w:%s,h:%s" % (file,width,height))
        img = lv.img_dsc_t({
            'header': {'always_zero': 0,"w": width, "h": height, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
            'data_size': len(data),
            'data': data
        })
        global_image_cache[file] = img
        return img
    def load_font(self,font_family, font_size):
        global global_font_cache
        if font_family + str(font_size) in global_font_cache:
            return global_font_cache[font_family + str(font_size)]
        if font_size % 2:
            candidates = [
                (font_family, font_size),
                (font_family, font_size-font_size%2),
                (font_family, font_size+font_size%2),
                ("montserrat", font_size-font_size%2),
                ("montserrat", font_size+font_size%2),
                ("montserrat", 16)
            ]
        else:
            candidates = [
                (font_family, font_size),
                ("montserrat", font_size),
                ("montserrat", 16)
            ]
        for (family, size) in candidates:
            try:
                if eval(f'lv.font_{family}_{size}'):
                    global_font_cache[font_family + str(font_size)] = eval(f'lv.font_{family}_{size}')
                    if family != font_family or size != font_size:
                        print(f'WARNING: lv.font_{family}_{size} is used!')
                    return eval(f'lv.font_{family}_{size}')
            except AttributeError:
                try:
                    load_font = lv.font_load(f"Z:ui/fonts/ui_font_{family}{size}.bin")
                    global_font_cache[font_family + str(font_size)] = load_font
                    print(f'loading font->ui_font_{family}{size}.bin')
                    return load_font
                except:
                    if family == font_family and size == font_size:
                        print(f'WARNING: lv.font_{family}_{size} is NOT supported!')