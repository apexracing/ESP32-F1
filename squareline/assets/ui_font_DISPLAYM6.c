/*******************************************************************************
 * Size: 6 px
 * Bpp: 4
 * Opts: --bpp 4 --size 6 --font F:/ESP32/squareline/assets/SFPRODISPLAYMEDIUM.OTF -o F:/ESP32/squareline/assets\ui_font_DISPLAYM6.c --format lvgl -r 0x20-0x7f --no-compress --no-prefilter
 ******************************************************************************/

#include "../ui.h"

#ifndef UI_FONT_DISPLAYM6
#define UI_FONT_DISPLAYM6 1
#endif

#if UI_FONT_DISPLAYM6

/*-----------------
 *    BITMAPS
 *----------------*/

/*Store the image of the glyphs*/
static LV_ATTRIBUTE_LARGE_CONST const uint8_t glyph_bitmap[] = {
    /* U+0020 " " */

    /* U+0021 "!" */
    0x72, 0x72, 0x41, 0x30,

    /* U+0022 "\"" */
    0x96, 0x14, 0x30,

    /* U+0023 "#" */
    0x7, 0x61, 0x5a, 0xb4, 0x99, 0xb2, 0x71, 0x60,

    /* U+0024 "$" */
    0x7, 0x40, 0x79, 0x82, 0x4c, 0x50, 0x15, 0x94,
    0x5a, 0x91,

    /* U+0025 "%" */
    0x89, 0x8, 0x5, 0x68, 0x10, 0x5, 0x58, 0x23,
    0x63, 0xa4,

    /* U+0026 "&" */
    0x29, 0x80, 0x1, 0xa6, 0x20, 0x84, 0x88, 0x6,
    0x78, 0x90,

    /* U+0027 "'" */
    0x94,

    /* U+0028 "(" */
    0x9, 0x45, 0x63, 0x45, 0x9,

    /* U+0029 ")" */
    0x80, 0x45, 0x27, 0x45, 0x80,

    /* U+002A "*" */
    0x1, 0x3, 0xa3, 0x39, 0x30,

    /* U+002B "+" */
    0x0, 0x0, 0x6, 0x20, 0x5b, 0x93, 0x6, 0x20,

    /* U+002C "," */
    0x10, 0x80, 0x20,

    /* U+002D "-" */
    0x58, 0x20,

    /* U+002E "." */
    0x40,

    /* U+002F "/" */
    0x8, 0x0, 0x80, 0x44, 0x8, 0x0, 0x80, 0x0,

    /* U+0030 "0" */
    0x3a, 0xa0, 0x90, 0x45, 0x90, 0x45, 0x3a, 0xa0,

    /* U+0031 "1" */
    0x5d, 0x1, 0x90, 0x9, 0x0, 0x90,

    /* U+0032 "2" */
    0x48, 0x90, 0x20, 0x90, 0x7, 0x40, 0x7b, 0x81,

    /* U+0033 "3" */
    0x48, 0xa0, 0x5, 0xa0, 0x30, 0x63, 0x48, 0x90,

    /* U+0034 "4" */
    0x6, 0xd0, 0x46, 0x90, 0x88, 0xd4, 0x0, 0x90,

    /* U+0035 "5" */
    0x69, 0x81, 0x87, 0x70, 0x30, 0x54, 0x49, 0x90,

    /* U+0036 "6" */
    0x3a, 0xa1, 0x87, 0x80, 0xa1, 0x45, 0x39, 0x91,

    /* U+0037 "7" */
    0x68, 0xd0, 0x1, 0x80, 0x9, 0x10, 0x28, 0x0,

    /* U+0038 "8" */
    0x58, 0x91, 0x3b, 0xb0, 0xa0, 0x55, 0x48, 0x91,

    /* U+0039 "9" */
    0x49, 0x90, 0xa0, 0x75, 0x38, 0xa4, 0x59, 0xa0,

    /* U+003A ":" */
    0x30, 0x0, 0x40,

    /* U+003B ";" */
    0x30, 0x10, 0x80, 0x20,

    /* U+003C "<" */
    0x0, 0x0, 0x5, 0x91, 0x5a, 0x0, 0x2, 0x91,
    0x0, 0x0,

    /* U+003D "=" */
    0x58, 0x82, 0x58, 0x82,

    /* U+003E ">" */
    0x10, 0x0, 0x39, 0x30, 0x2, 0xc1, 0x47, 0x10,
    0x0, 0x0,

    /* U+003F "?" */
    0x68, 0x71, 0x38, 0x7, 0x0, 0x40,

    /* U+0040 "@" */
    0x17, 0x68, 0x30, 0x72, 0x66, 0x70, 0x76, 0x19,
    0x60, 0x54, 0x78, 0x50, 0x5, 0x63, 0x0,

    /* U+0041 "A" */
    0x8, 0x70, 0x8, 0x80, 0x59, 0xa4, 0xa0, 0x9,

    /* U+0042 "B" */
    0x98, 0xa2, 0x97, 0xb1, 0x90, 0x36, 0x98, 0x92,

    /* U+0043 "C" */
    0x3a, 0x86, 0xa1, 0x3, 0xa1, 0x2, 0x3a, 0x86,

    /* U+0044 "D" */
    0x98, 0xa4, 0x90, 0xb, 0x90, 0xb, 0x99, 0xa4,

    /* U+0045 "E" */
    0x98, 0x80, 0x98, 0x70, 0x90, 0x0, 0x99, 0x80,

    /* U+0046 "F" */
    0x98, 0x80, 0x90, 0x0, 0x98, 0x70, 0x90, 0x0,

    /* U+0047 "G" */
    0x3a, 0x85, 0xa, 0x10, 0x50, 0xa1, 0x5a, 0x3,
    0xb8, 0x70,

    /* U+0048 "H" */
    0x90, 0xa, 0x98, 0x8c, 0x90, 0xa, 0x90, 0xa,

    /* U+0049 "I" */
    0x90, 0x90, 0x90, 0x90,

    /* U+004A "J" */
    0x0, 0xa0, 0xa, 0x10, 0xa7, 0x95,

    /* U+004B "K" */
    0x90, 0x83, 0x99, 0x30, 0x98, 0x80, 0x90, 0x75,

    /* U+004C "L" */
    0x90, 0x0, 0x90, 0x0, 0x90, 0x0, 0x99, 0x80,

    /* U+004D "M" */
    0x95, 0x4, 0xa9, 0x90, 0x99, 0x95, 0x66, 0x99,
    0xd, 0x9,

    /* U+004E "N" */
    0x95, 0xa, 0x99, 0x2a, 0x91, 0xaa, 0x90, 0x2c,

    /* U+004F "O" */
    0x3b, 0xa7, 0xa, 0x10, 0xa1, 0xa1, 0xa, 0x13,
    0xaa, 0x80,

    /* U+0050 "P" */
    0x98, 0xa0, 0x90, 0x64, 0x98, 0x80, 0x90, 0x0,

    /* U+0051 "Q" */
    0x3a, 0xa8, 0xa, 0x10, 0xa1, 0xa1, 0x3a, 0x13,
    0xab, 0xa0, 0x0, 0x5, 0x0,

    /* U+0052 "R" */
    0x98, 0x91, 0x90, 0x55, 0x98, 0xc1, 0x90, 0x83,

    /* U+0053 "S" */
    0x48, 0x91, 0x77, 0x20, 0x12, 0x94, 0x58, 0x92,

    /* U+0054 "T" */
    0x7c, 0x93, 0x8, 0x10, 0x8, 0x10, 0x8, 0x10,

    /* U+0055 "U" */
    0x90, 0xa, 0x90, 0xa, 0x91, 0xa, 0x29, 0x94,

    /* U+0056 "V" */
    0xa0, 0x19, 0x54, 0x63, 0x9, 0xa0, 0x9, 0x70,

    /* U+0057 "W" */
    0xa0, 0x94, 0x45, 0x73, 0x98, 0x81, 0x2a, 0x58,
    0x90, 0xd, 0x6, 0x70,

    /* U+0058 "X" */
    0x84, 0x46, 0xa, 0x90, 0xa, 0xa0, 0x83, 0x56,

    /* U+0059 "Y" */
    0x92, 0x56, 0x1a, 0xa0, 0x7, 0x40, 0x6, 0x30,

    /* U+005A "Z" */
    0x58, 0xc4, 0x2, 0x80, 0xa, 0x0, 0x9a, 0x83,

    /* U+005B "[" */
    0x69, 0x63, 0x63, 0x63, 0x69,

    /* U+005C "\\" */
    0x80, 0x8, 0x0, 0x44, 0x0, 0x80, 0x8, 0x0,

    /* U+005D "]" */
    0x87, 0x27, 0x27, 0x27, 0x87,

    /* U+005E "^" */
    0x5, 0x7, 0x44,

    /* U+005F "_" */
    0x17, 0x74,

    /* U+0060 "`" */
    0x8, 0x0,

    /* U+0061 "a" */
    0x58, 0x75, 0x6b, 0x87, 0xb0,

    /* U+0062 "b" */
    0x90, 0x0, 0xa8, 0x90, 0xa0, 0x72, 0xa8, 0x90,

    /* U+0063 "c" */
    0x58, 0x7a, 0x1, 0x58, 0x70,

    /* U+0064 "d" */
    0x0, 0x81, 0x68, 0xc1, 0xa0, 0xa1, 0x68, 0xc1,

    /* U+0065 "e" */
    0x57, 0x6a, 0x69, 0x58, 0x70,

    /* U+0066 "f" */
    0x57, 0xb6, 0x72, 0x72,

    /* U+0067 "g" */
    0x67, 0xb1, 0xa0, 0xa1, 0x68, 0xc1, 0x48, 0x80,

    /* U+0068 "h" */
    0x90, 0x0, 0xa8, 0x90, 0xa0, 0x90, 0x90, 0x90,

    /* U+0069 "i" */
    0x40, 0xa0, 0xa0, 0xa0,

    /* U+006A "j" */
    0x4, 0x0, 0xa0, 0xa, 0x0, 0xa0, 0x19, 0x0,

    /* U+006B "k" */
    0x90, 0x0, 0x94, 0x70, 0xac, 0x0, 0x92, 0x90,

    /* U+006C "l" */
    0x99, 0x99,

    /* U+006D "m" */
    0xa8, 0xa8, 0x6a, 0xa, 0xa, 0xa0, 0x90, 0xa0,

    /* U+006E "n" */
    0xa8, 0x9a, 0xa, 0xa0, 0xa0,

    /* U+006F "o" */
    0x58, 0x70, 0xa0, 0x90, 0x58, 0x70,

    /* U+0070 "p" */
    0xa8, 0x90, 0xa0, 0x82, 0xa8, 0x90, 0xa0, 0x0,

    /* U+0071 "q" */
    0x68, 0xc1, 0xa0, 0xa1, 0x68, 0xc1, 0x0, 0x81,

    /* U+0072 "r" */
    0xa7, 0xa0, 0xa0,

    /* U+0073 "s" */
    0x77, 0x54, 0x84, 0x67, 0x60,

    /* U+0074 "t" */
    0x31, 0xb6, 0x72, 0x57,

    /* U+0075 "u" */
    0xa0, 0x9a, 0xa, 0x68, 0xc0,

    /* U+0076 "v" */
    0xa0, 0xa6, 0x66, 0x1e, 0x0,

    /* U+0077 "w" */
    0x93, 0xa5, 0x37, 0x88, 0x80, 0x3a, 0x4a, 0x0,

    /* U+0078 "x" */
    0x84, 0x71, 0xe0, 0x85, 0x70,

    /* U+0079 "y" */
    0xa0, 0xa5, 0x66, 0xd, 0x15, 0x70,

    /* U+007A "z" */
    0x5a, 0x70, 0x90, 0x99, 0x40,

    /* U+007B "{" */
    0x19, 0x45, 0xb1, 0x45, 0x19,

    /* U+007C "|" */
    0x34, 0x34, 0x34, 0x34, 0x34,

    /* U+007D "}" */
    0x92, 0x45, 0x1c, 0x45, 0x92,

    /* U+007E "~" */
    0x48, 0x11, 0x21, 0x91
};


/*---------------------
 *  GLYPH DESCRIPTION
 *--------------------*/

static const lv_font_fmt_txt_glyph_dsc_t glyph_dsc[] = {
    {.bitmap_index = 0, .adv_w = 0, .box_w = 0, .box_h = 0, .ofs_x = 0, .ofs_y = 0} /* id = 0 reserved */,
    {.bitmap_index = 0, .adv_w = 19, .box_w = 0, .box_h = 0, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 0, .adv_w = 27, .box_w = 2, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 4, .adv_w = 40, .box_w = 3, .box_h = 2, .ofs_x = 0, .ofs_y = 2},
    {.bitmap_index = 7, .adv_w = 59, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 15, .adv_w = 60, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 25, .adv_w = 73, .box_w = 5, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 35, .adv_w = 65, .box_w = 5, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 45, .adv_w = 21, .box_w = 1, .box_h = 2, .ofs_x = 0, .ofs_y = 2},
    {.bitmap_index = 46, .adv_w = 33, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 51, .adv_w = 33, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 56, .adv_w = 46, .box_w = 3, .box_h = 3, .ofs_x = 0, .ofs_y = 2},
    {.bitmap_index = 61, .adv_w = 60, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 69, .adv_w = 25, .box_w = 2, .box_h = 3, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 72, .adv_w = 42, .box_w = 3, .box_h = 1, .ofs_x = 0, .ofs_y = 1},
    {.bitmap_index = 74, .adv_w = 25, .box_w = 2, .box_h = 1, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 75, .adv_w = 33, .box_w = 3, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 83, .adv_w = 60, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 91, .adv_w = 44, .box_w = 3, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 97, .adv_w = 56, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 105, .adv_w = 58, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 113, .adv_w = 60, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 121, .adv_w = 58, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 129, .adv_w = 59, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 137, .adv_w = 53, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 145, .adv_w = 59, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 153, .adv_w = 59, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 161, .adv_w = 25, .box_w = 2, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 164, .adv_w = 25, .box_w = 2, .box_h = 4, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 168, .adv_w = 60, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 178, .adv_w = 60, .box_w = 4, .box_h = 2, .ofs_x = 0, .ofs_y = 1},
    {.bitmap_index = 182, .adv_w = 60, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 192, .adv_w = 49, .box_w = 3, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 198, .adv_w = 84, .box_w = 6, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 213, .adv_w = 63, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 221, .adv_w = 59, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 229, .adv_w = 67, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 237, .adv_w = 66, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 245, .adv_w = 54, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 253, .adv_w = 51, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 261, .adv_w = 69, .box_w = 5, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 271, .adv_w = 68, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 279, .adv_w = 23, .box_w = 2, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 283, .adv_w = 50, .box_w = 3, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 289, .adv_w = 61, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 297, .adv_w = 51, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 305, .adv_w = 81, .box_w = 5, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 315, .adv_w = 68, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 323, .adv_w = 71, .box_w = 5, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 333, .adv_w = 57, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 341, .adv_w = 71, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 354, .adv_w = 59, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 362, .adv_w = 58, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 370, .adv_w = 56, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 378, .adv_w = 67, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 386, .adv_w = 62, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 394, .adv_w = 90, .box_w = 6, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 406, .adv_w = 63, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 414, .adv_w = 61, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 422, .adv_w = 60, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 430, .adv_w = 33, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 435, .adv_w = 33, .box_w = 3, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 443, .adv_w = 33, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 448, .adv_w = 43, .box_w = 3, .box_h = 2, .ofs_x = 0, .ofs_y = 2},
    {.bitmap_index = 451, .adv_w = 39, .box_w = 4, .box_h = 1, .ofs_x = -1, .ofs_y = -1},
    {.bitmap_index = 453, .adv_w = 47, .box_w = 3, .box_h = 1, .ofs_x = 0, .ofs_y = 4},
    {.bitmap_index = 455, .adv_w = 50, .box_w = 3, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 460, .adv_w = 55, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 468, .adv_w = 50, .box_w = 3, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 473, .adv_w = 55, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 481, .adv_w = 51, .box_w = 3, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 486, .adv_w = 31, .box_w = 2, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 490, .adv_w = 54, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 498, .adv_w = 53, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 506, .adv_w = 21, .box_w = 2, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 510, .adv_w = 21, .box_w = 3, .box_h = 5, .ofs_x = -1, .ofs_y = -1},
    {.bitmap_index = 518, .adv_w = 48, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 526, .adv_w = 21, .box_w = 1, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 528, .adv_w = 79, .box_w = 5, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 536, .adv_w = 52, .box_w = 3, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 541, .adv_w = 52, .box_w = 4, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 547, .adv_w = 54, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 555, .adv_w = 54, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 563, .adv_w = 32, .box_w = 2, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 566, .adv_w = 46, .box_w = 3, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 571, .adv_w = 31, .box_w = 2, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 575, .adv_w = 52, .box_w = 3, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 580, .adv_w = 48, .box_w = 3, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 585, .adv_w = 71, .box_w = 5, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 593, .adv_w = 47, .box_w = 3, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 598, .adv_w = 49, .box_w = 3, .box_h = 4, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 604, .adv_w = 46, .box_w = 3, .box_h = 3, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 609, .adv_w = 33, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 614, .adv_w = 33, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 619, .adv_w = 33, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 624, .adv_w = 60, .box_w = 4, .box_h = 2, .ofs_x = 0, .ofs_y = 1}
};

/*---------------------
 *  CHARACTER MAPPING
 *--------------------*/



/*Collect the unicode lists and glyph_id offsets*/
static const lv_font_fmt_txt_cmap_t cmaps[] =
{
    {
        .range_start = 32, .range_length = 95, .glyph_id_start = 1,
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
    .bpp = 4,
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
const lv_font_t ui_font_DISPLAYM6 = {
#else
lv_font_t ui_font_DISPLAYM6 = {
#endif
    .get_glyph_dsc = lv_font_get_glyph_dsc_fmt_txt,    /*Function pointer to get glyph's data*/
    .get_glyph_bitmap = lv_font_get_bitmap_fmt_txt,    /*Function pointer to get glyph's bitmap*/
    .line_height = 6,          /*The maximum line height required by the font*/
    .base_line = 1,             /*Baseline measured from the bottom of the line*/
#if !(LVGL_VERSION_MAJOR == 6 && LVGL_VERSION_MINOR == 0)
    .subpx = LV_FONT_SUBPX_NONE,
#endif
#if LV_VERSION_CHECK(7, 4, 0) || LVGL_VERSION_MAJOR >= 8
    .underline_position = -1,
    .underline_thickness = 0,
#endif
    .dsc = &font_dsc           /*The custom font data. Will be accessed by `get_glyph_bitmap/dsc` */
};



#endif /*#if UI_FONT_DISPLAYM6*/

