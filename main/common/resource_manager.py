import lvgl as lv
from common import fs_driver
import lodepng


class ResourceManager:
    _instance=None
    def __new__(cls, *args, **kwargs):
        """
        单例资源管理器，可直接new ResouceManger,引用同一个实例
        :param args:
        :param kwargs:
        """
        if not cls._instance:
            cls._instance=super(ResourceManager,cls).__new__(cls)
        return cls._instance
    def __init__(self):
        self.global_image_cache = {}
        self.global_font_cache = {}
        self.global_raw_cache={}
        lv.init()
        fs_drv = lv.fs_drv_t()
        fs_driver.fs_register(fs_drv, 'Z')
        print("初始化文件系统Z:盘")

    @staticmethod
    def __load_png(filepath):
        with open(filepath, "rb") as f:
            png_data = f.read()
            info, data = lodepng.decode(png_data)
        return info, data

    def load_raw(self,file):
        """
        用于lottie文件缓存
        :param file:
        :return:
        """
        if file in self.global_raw_cache:
            return self.global_raw_cache[file]
        with open(file, 'r') as f:
            raw_data = f.read()
        return raw_data

    def load_img(self, file):
        """
        只支持png格式图片
        :param file:
        :return:
        """
        if file in self.global_image_cache:
            return self.global_image_cache[file]
        info, data = self.__load_png(file)
        img = lv.img_dsc_t({
            'data_size': len(data),
            'data': data
        })
        self.global_image_cache[file] = img
        return img
    def load_font(self,font_family, font_size):
        if font_family + str(font_size) in self.global_font_cache:
            return self.global_font_cache[font_family + str(font_size)]
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
                    self.global_font_cache[font_family + str(font_size)] = eval(f'lv.font_{family}_{size}')
                    if family != font_family or size != font_size:
                        print(f'WARNING: lv.font_{family}_{size} is used!')
                    return eval(f'lv.font_{family}_{size}')
            except AttributeError:
                try:
                    load_font = lv.font_load(f"Z:ui/fonts/ui_font_{family}{size}.bin")
                    self.global_font_cache[font_family + str(font_size)] = load_font
                    return load_font
                except:
                    if family == font_family and size == font_size:
                        print(f'WARNING: lv.font_{family}_{size} is NOT supported!')