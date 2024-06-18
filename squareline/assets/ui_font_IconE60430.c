/*******************************************************************************
 * Size: 30 px
 * Bpp: 2
 * Opts: --bpp 2 --size 30 --font E:/github/esp32/squareline/assets/iconfont.ttf -o E:/github/esp32/squareline/assets\ui_font_IconE60430.c --format lvgl --symbols  --no-compress --no-prefilter
 ******************************************************************************/

#include "../ui.h"

#ifndef UI_FONT_ICONE60430
#define UI_FONT_ICONE60430 1
#endif

#if UI_FONT_ICONE60430

/*-----------------
 *    BITMAPS
 *----------------*/

/*Store the image of the glyphs*/
static LV_ATTRIBUTE_LARGE_CONST const uint8_t glyph_bitmap[] = {
    /* U+E604 "" */
    0x0, 0x2f, 0x80, 0x0, 0xe, 0x5b, 0x0, 0x2,
    0x80, 0x38, 0x0, 0x34, 0x1, 0xc0, 0x3, 0x40,
    0x1c, 0x0, 0x34, 0x1, 0xc0, 0x3, 0x40, 0x1c,
    0x0, 0x34, 0x1, 0xc0, 0x3, 0x40, 0x1c, 0x0,
    0x34, 0xf5, 0xc0, 0x3, 0x4f, 0x5c, 0x0, 0x34,
    0xf5, 0xc0, 0x3, 0x4f, 0x5c, 0x0, 0x34, 0xf5,
    0xc0, 0x3, 0x4f, 0x5c, 0x0, 0x34, 0xf5, 0xc0,
    0x3, 0x4f, 0x5c, 0x0, 0xe0, 0xf8, 0xb0, 0x2c,
    0xbf, 0xe3, 0x83, 0x5f, 0xff, 0x5c, 0x33, 0xff,
    0xfc, 0xc3, 0x3f, 0xff, 0xcc, 0x32, 0xff, 0xf8,
    0xc2, 0x8f, 0xff, 0x28, 0xd, 0x2f, 0x87, 0x0,
    0x78, 0x2, 0xd0, 0x1, 0xff, 0xf4, 0x0, 0x0,
    0x50, 0x0
};


/*---------------------
 *  GLYPH DESCRIPTION
 *--------------------*/

static const lv_font_fmt_txt_glyph_dsc_t glyph_dsc[] = {
    {.bitmap_index = 0, .adv_w = 0, .box_w = 0, .box_h = 0, .ofs_x = 0, .ofs_y = 0} /* id = 0 reserved */,
    {.bitmap_index = 0, .adv_w = 480, .box_w = 14, .box_h = 28, .ofs_x = 8, .ofs_y = -3}
};

/*---------------------
 *  CHARACTER MAPPING
 *--------------------*/



/*Collect the unicode lists and glyph_id offsets*/
static const lv_font_fmt_txt_cmap_t cmaps[] =
{
    {
        .range_start = 58884, .range_length = 1, .glyph_id_start = 1,
        .unicode_list = NULL, .glyph_id_ofs_list = NULL, .list_length = 0, .type = LV_FONT_FMT_TXT_CMAP_FORMAT0_TINY
    }
};



/*--------------------
 *  ALL CUSTOM DATA
 *--------------------*/

#if LV_VERSION_CHECK(8, 0, 0)
/*Store all the custom data of the font*/
static  lv_font_fmt_txt_glyph_cache_t cache;
static const lv_font_fmt_txt_dsc_t font_dsc = {
#else
static lv_font_fmt_txt_dsc_t font_dsc = {
#endif
    .glyph_bitmap = glyph_bitmap,
    .glyph_dsc = glyph_dsc,
    .cmaps = cmaps,
    .kern_dsc = NULL,
    .kern_scale = 0,
    .cmap_num = 1,
    .bpp = 2,
    .kern_classes = 0,
    .bitmap_format = 0,
#if LV_VERSION_CHECK(8, 0, 0)
    .cache = &cache
#endif
};


/*-----------------
 *  PUBLIC FONT
 *----------------*/

/*Initialize a public general font descriptor*/
#if LV_VERSION_CHECK(8, 0, 0)
const lv_font_t ui_font_IconE60430 = {
#else
lv_font_t ui_font_IconE60430 = {
#endif
    .get_glyph_dsc = lv_font_get_glyph_dsc_fmt_txt,    /*Function pointer to get glyph's data*/
    .get_glyph_bitmap = lv_font_get_bitmap_fmt_txt,    /*Function pointer to get glyph's bitmap*/
    .line_height = 28,          /*The maximum line height required by the font*/
    .base_line = 3,             /*Baseline measured from the bottom of the line*/
#if !(LVGL_VERSION_MAJOR == 6 && LVGL_VERSION_MINOR == 0)
    .subpx = LV_FONT_SUBPX_NONE,
#endif
#if LV_VERSION_CHECK(7, 4, 0) || LVGL_VERSION_MAJOR >= 8
    .underline_position = 0,
    .underline_thickness = 0,
#endif
    .dsc = &font_dsc           /*The custom font data. Will be accessed by `get_glyph_bitmap/dsc` */
};



#endif /*#if UI_FONT_ICONE60430*/

