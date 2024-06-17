/*******************************************************************************
 * Size: 14 px
 * Bpp: 2
 * Opts: --bpp 2 --size 14 --font F:/ESP32/squareline/assets/race_icon.ttf -o F:/ESP32/squareline/assets\ui_font_ceilusunit.c --format lvgl --symbols  --no-compress --no-prefilter
 ******************************************************************************/

#include "../ui.h"

#ifndef UI_FONT_CEILUSUNIT
#define UI_FONT_CEILUSUNIT 1
#endif

#if UI_FONT_CEILUSUNIT

/*-----------------
 *    BITMAPS
 *----------------*/

/*Store the image of the glyphs*/
static LV_ATTRIBUTE_LARGE_CONST const uint8_t glyph_bitmap[] = {
    /* U+E606 "" */
    0x0, 0x0, 0x0, 0x0, 0x0, 0xfe, 0x0, 0x7f,
    0xe0, 0x3c, 0x38, 0x1e, 0x7, 0x83, 0x42, 0xc3,
    0x80, 0xc, 0x38, 0x28, 0x70, 0x0, 0x41, 0xef,
    0x7, 0x0, 0x0, 0x6, 0x80, 0x70, 0x0, 0x0,
    0x0, 0x7, 0x0, 0x0, 0x0, 0x0, 0x70, 0x0,
    0x0, 0x0, 0x7, 0x0, 0x0, 0x0, 0x0, 0x70,
    0x0, 0x0, 0x0, 0x3, 0x0, 0xc, 0x0, 0x0,
    0x2c, 0x2, 0xc0, 0x0, 0x0, 0xfa, 0xf4, 0x0,
    0x0, 0x1, 0xa8, 0x0
};


/*---------------------
 *  GLYPH DESCRIPTION
 *--------------------*/

static const lv_font_fmt_txt_glyph_dsc_t glyph_dsc[] = {
    {.bitmap_index = 0, .adv_w = 0, .box_w = 0, .box_h = 0, .ofs_x = 0, .ofs_y = 0} /* id = 0 reserved */,
    {.bitmap_index = 0, .adv_w = 263, .box_w = 18, .box_h = 15, .ofs_x = -1, .ofs_y = -2}
};

/*---------------------
 *  CHARACTER MAPPING
 *--------------------*/



/*Collect the unicode lists and glyph_id offsets*/
static const lv_font_fmt_txt_cmap_t cmaps[] =
{
    {
        .range_start = 58886, .range_length = 1, .glyph_id_start = 1,
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
const lv_font_t ui_font_ceilusunit = {
#else
lv_font_t ui_font_ceilusunit = {
#endif
    .get_glyph_dsc = lv_font_get_glyph_dsc_fmt_txt,    /*Function pointer to get glyph's data*/
    .get_glyph_bitmap = lv_font_get_bitmap_fmt_txt,    /*Function pointer to get glyph's bitmap*/
    .line_height = 15,          /*The maximum line height required by the font*/
    .base_line = 2,             /*Baseline measured from the bottom of the line*/
#if !(LVGL_VERSION_MAJOR == 6 && LVGL_VERSION_MINOR == 0)
    .subpx = LV_FONT_SUBPX_NONE,
#endif
#if LV_VERSION_CHECK(7, 4, 0) || LVGL_VERSION_MAJOR >= 8
    .underline_position = 0,
    .underline_thickness = 0,
#endif
    .dsc = &font_dsc           /*The custom font data. Will be accessed by `get_glyph_bitmap/dsc` */
};



#endif /*#if UI_FONT_CEILUSUNIT*/

