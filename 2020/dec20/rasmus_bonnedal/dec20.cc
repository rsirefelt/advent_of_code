#include "ctl.hh"

#include <iostream>
#include <sstream>
#include <assert.h>
#include <math.h>

using boolvec = std::vector<bool>;
using intvec = std::vector<int>;

struct tile_t {
    int id;
    int borders[4];
    std::vector<boolvec> data;
    int edges;
    int rot;
    bool flipx;
    bool flipy;
    
};

using indata_t = std::vector<tile_t>;

int horiz_border(boolvec& bv) {
    int border = 0;
    for (bool b: bv) {
        border <<= 1;
        if (b) border |= 1;
    }
    return border;
}

int vert_border(std::vector<boolvec>& vbv, bool front) {
    int border = 0;
    for (auto& bv: vbv) {
        border <<= 1;
        if (front ? bv.front() : bv.back()) border |= 1;
    }
    return border;
}

tile_t parse_tile(const std::string& s) {
    tile_t retval;
    auto ss = split(s, "\n");
    retval.id = std::stoi(split(ss[0], " ")[1]);
    for (int i = 1; i < ss.size(); ++i) {
        retval.data.push_back(map([](char c) {
            return c == '#';
            }, ss[i]));
    }
    retval.borders[0] = horiz_border(retval.data.front());
    retval.borders[1] = vert_border(retval.data, false);
    retval.borders[2] = horiz_border(retval.data.back());
    retval.borders[3] = vert_border(retval.data, true);
    retval.rot = 0;
    retval.flipx = false;
    retval.flipy = false;
    return retval;
}

indata_t parse(const std::string& filename) {
    return map(parse_tile, split(read_file(filename), "\n\n"));
}

int bit_rev(int x) {
    int retval = 0;
    for (int i = 0; i < 10; ++i) {
        retval <<= 1;
        if ((x >> i) & 1) retval |= 1;
    }
    return retval;
}

struct DefInt {
    int i = 0;
};

bool tile_match(tile_t& t1, tile_t& t2) {
    std::set<int> borders1;
    std::set<int> borders2;
    for (int i = 0; i < 4; ++i) {
        borders1.insert(t1.borders[i]);
        borders1.insert(bit_rev(t1.borders[i]));
        borders2.insert(t2.borders[i]);
        borders2.insert(bit_rev(t2.borders[i]));
    }

    std::set<int> borders = borders1;
    for (int x: borders2) borders.insert(x);
    if (borders.size() == 16) return false;
    assert(borders.size() == 14);
    return true;
}

void align(tile_t& t1, tile_t& t2) {
/*
    --0-->
   | #.#. |
   3 ..## 1
   | ...# |
  \|/#..#\|/
    --2-->
*/
    int rot1 = 0;
    int rot2 = 0;
    bool flipy1 = false;
    bool flipy2 = false;
    bool flipx2 = false;
    for (int i1 = 0; i1 < 4; ++i1) {
        for (int i2 = 0; i2 < 4; ++i2) {
            if (t1.borders[i1] == t2.borders[i2]) {
                if (i1 == 0 || i1 == 2) rot1 = 1;
                if (i2 == 0 || i2 == 2) rot2 = 1;
                if (i1 == 3 || i1 == 2) flipy1 = true;
                if (i2 == 1 || i2 == 0) flipy2 = true;
                flipx2 = t1.flipx;
            } else if (t1.borders[i1] == bit_rev(t2.borders[i2])) {
                if (i1 == 0 || i1 == 2) rot1 = 1;
                if (i2 == 0 || i2 == 2) rot2 = 1;
                if (i1 == 3 || i1 == 2) flipy1 = true;
                if (i2 == 1 || i2 == 0) flipy2 = true;
                flipx2 = !t1.flipx;
            }
        }
    }
    t1.rot = rot1;
    t1.flipy = flipy1;
    t2.rot = rot2;
    t2.flipy = flipy2;
    t2.flipx = flipx2;

}

bool check_seamonster(const std::vector<boolvec>& image, std::vector<boolvec>& seamonster, int x, int y) {
    if (y + seamonster.size() > image.size()) return false;
    if (x + seamonster[0].size() > image[0].size()) return false;
    for (int yp = 0; yp < seamonster.size(); ++yp) {
        for (int xp = 0; xp < seamonster[0].size(); ++xp) {
            if (seamonster[yp][xp] && !image[y+yp][x+xp]) return false;
        }
    }
    return true;
}

using image_t = std::vector<boolvec>;
image_t rot(const image_t& image) {
    image_t retval;
    retval.resize(image.size(), boolvec(image[0].size()));
    for (int y = 0; y < image.size(); ++y) {
        for (int x = 0; x < image.size(); ++x) {
            retval[y][x] = image[image.size()-1-x][y];
        }    
    }
    return retval;
}

image_t flipx(const image_t& image) {
    image_t retval;
    retval.resize(image.size(), boolvec(image[0].size()));
    for (int y = 0; y < image.size(); ++y) {
        for (int x = 0; x < image.size(); ++x) {
            retval[y][x] = image[image.size()-1-y][x];
        }    
    }
    return retval;
}

image_t flipy(const image_t& image) {
    image_t retval;
    retval.resize(image.size(), boolvec(image[0].size()));
    for (int y = 0; y < image.size(); ++y) {
        for (int x = 0; x < image.size(); ++x) {
            retval[y][x] = image[y][image[0].size() - 1 - x];
        }    
    }
    return retval;
}

int count_seamonsters(const image_t& image) {
    std::string seamonster_s =
        "                  # \n"
        "#    ##    ##    ###\n"
        " #  #  #  #  #  #   \n";
    std::vector<boolvec> seamonster;

    for (auto& line: split(seamonster_s, "\n")) {
        seamonster.push_back(boolvec());
        for (auto c: line) {
            seamonster.back().push_back(c == '#');
        }
    }

    int seamonsters = 0;
    int ones = 0;
    for (int y = 0; y < image.size(); ++y) {
        for (int x = 0; x < image[0].size(); ++x) {
            if (check_seamonster(image, seamonster, x, y)) {
                seamonsters++;
                std::cout << "Found seamonster " << x << ", " << y << std::endl;
            }
            if (image[y][x]) ones++;
        }
    }
    std::cout << "Ones: " << ones - seamonsters*15 << std::endl;
    return seamonsters;
}

void print_image(const image_t& image, int dim) {
    for (int y = 0; y < image.size(); ++y) {
        if (y % 8 == 0) {
            std::cout << "  ";
            for (int x = 0; x < image.size()+dim; ++x) {
                std::cout << (x % 9 == 0 ? '+' : '-');

            }
            std::cout << std::endl;
        }
        std::cout << y;
        for (int x = 0; x < image.size(); ++x) {
            if (x % 8 == 0) std::cout << "|";
            std::cout << (image[y][x] ? '#' : '.');
        }
        std::cout << std::endl;
    }
}

void align_y(tile_t& t1, tile_t& t2, bool& flipx1, bool& flipx2) {
/*
    --0-->
   | #.#. |
   3 ..## 1
   | ...# |
  \|/#..#\|/
    --2-->
*/
    if (t1.id == 1747) {
        int apa = 0;
    }
    flipx1 = false;
    flipx2 = false;
    for (int i1 = 0; i1 < 4; ++i1) {
        for (int i2 = 0; i2 < 4; ++i2) {
            if (t1.borders[i1] == t2.borders[i2]) {
                if (i1 == 0 || i1 == 3) {
                    if (!t1.flipx) flipx1 = true;
                }
                if (i2 == 1 || i2 == 2) {
                    if (!t2.flipx) flipx2 = true;
                };
                return;
            } else if (t1.borders[i1] == bit_rev(t2.borders[i2])) {
                if (i1 == 0 || i1 == 3) {
                    if (!t1.flipx) flipx1 = true;
                }
                if (i2 == 1 || i2 == 2) {
                    if (!t2.flipx) flipx2 = true;
                };
                return;
            }
        }
    }
    assert(false);
}

bool get_tile_pix(const tile_t& tile, int x, int y) {
    int xp = x;
    int yp = y;
    if (tile.flipx) {
        yp = 9 - yp;
    }
    if (tile.flipy) {
        xp = 9 - xp;
    }
    if (tile.rot == 1) {
        std::swap(xp, yp);
        yp = 9 - yp;
    }
    return tile.data[yp][xp];
}

int64_t part1(indata_t& ind) {
    std::map<int, std::set<int>> bordermap;
    for (auto& tile: ind) {
        for (int i = 0; i < 4; ++i) {
            bordermap[tile.borders[i]].insert(tile.id);
            bordermap[bit_rev(tile.borders[i])].insert(tile.id);
        }
    }
    int ones = 0;
    for (auto& bm: bordermap) {
        if (bm.second.size() == 1) ones++;
    }
    int64_t value = 1;
    int corner_id;
    for (auto& tile: ind) {
        int edges = 0;
        for (int i = 0; i < 4; ++i) {
            if (bordermap[tile.borders[i]].size() == 1) edges++;
            if (bordermap[bit_rev(tile.borders[i])].size() == 1) edges++;
        }
        if (edges == 4) {
            value *= tile.id;
            corner_id = tile.id;
        }
        tile.edges = edges / 2;
    }

    std::set<int> used_tiles;
    std::vector<intvec> tiles;
    std::map<int, int> tilemap;
    int dim = sqrt(ind.size());
    std::cout << dim << std::endl;

    for (int i = 0; i < ind.size(); ++i) {
        tilemap[ind[i].id] = i;
    }

    for (int y = 0; y < dim; ++y) {
        tiles.push_back(intvec());
        for (int x = 0; x < dim; ++x) {
            int id=-1;
            if (y == 0 && x == 0) {
                id = corner_id;
            } else {
                int edges = 0;
                bool y_edge = y == 0 || y == dim - 1;
                bool x_edge = x == 0 || x == dim - 1;
                if (y_edge) edges++;
                if (x_edge) edges++;
                if (edges == 2) {
                    int ref_id = (x > 0) ? tiles[y][x-1] : tiles[y-1][x];
                    tile_t& ref_tile = ind[tilemap[ref_id]];
                    // Find tile with edges == 2 && edge_match(ref_id)
                    for (auto& tile: ind) {
                        if (!in(tile.id, used_tiles) && tile.edges == 2 && tile_match(ref_tile, tile)) {
                            id = tile.id;
                            std::cout << "x = " << x << ", y = " << y << ", found tile: " << id << std::endl;
                        }
                    }
                } else if (edges == 1) {
                    int ref_id = y_edge ? tiles[y][x-1] : tiles[y-1][x];
                    tile_t& ref_tile = ind[tilemap[ref_id]];
                    // Find tile with edges == 1 && edge_match(ref_id)
                    for (auto& tile: ind) {
                        if (!in(tile.id, used_tiles) && tile.edges == 1 && tile_match(ref_tile, tile)) {
                            id = tile.id;
                            std::cout << "x = " << x << ", y = " << y << ", found tile: " << id << std::endl;
                        }
                    }
                } else { // edges == 0
                    int ref_id_1 = tiles[y][x-1];
                    int ref_id_2 = tiles[y-1][x];
                    tile_t& ref_tile_1 = ind[tilemap[ref_id_1]];
                    tile_t& ref_tile_2 = ind[tilemap[ref_id_2]];
                    // Find tile with edges == 0 && edge_match(ref_id_1, ref_id_2)
                   for (auto& tile: ind) {
                        if (!in(tile.id, used_tiles) && tile.edges == 0 && tile_match(ref_tile_1, tile) && tile_match(ref_tile_2, tile)) {
                            id = tile.id;
                            std::cout << "x = " << x << ", y = " << y << ", found tile: " << id << std::endl;
                        }
                    }
                 }

            }
            assert(id != -1);
            std::cout << id << ", ";
            tiles.back().push_back(id);
            used_tiles.insert(id);
        }
        std::cout << std::endl;
    }

    // Find rot/flip
    for (int y = 0; y < dim; ++y) {
        for (int x = 0; x < dim - 1; ++x) {
            align(ind[tilemap[tiles[y][x]]], ind[tilemap[tiles[y][x+1]]]);
        }
        if (y > 0) {
            bool flipx1, flipx2;
            tile_t& tile1 = ind[tilemap[tiles[y-1][0]]];
            tile_t& tile2 = ind[tilemap[tiles[y][0]]];
            
            align_y(tile1, tile2, flipx1, flipx2);
            for (int x = 0; x < dim; ++x) {
                if (flipx1) {
                    ind[tilemap[tiles[y-1][x]]].flipx = !ind[tilemap[tiles[y-1][x]]].flipx;
                }
                if (flipx2) {
                    ind[tilemap[tiles[y][x]]].flipx = !ind[tilemap[tiles[y][x]]].flipx;
                }
            }
        }
    }

    for (int y = 0; y < dim; ++y) {
        for (int x = 0; x < dim; ++x) {
            tile_t& tile = ind[tilemap[tiles[y][x]]];
            std::cout << tile.id << ": R" << tile.rot << " fx: " << (tile.flipx ? 1 : 0) << " fy: " << (tile.flipy ? 1 : 0) << ", "; 
        }
        std::cout << std::endl;
    }

    // Merge
    std::vector<boolvec> image;
    image.resize(dim * 8, boolvec(dim * 8));
    for (int tiley = 0; tiley < dim; ++tiley) {
        for (int tilex = 0; tilex < dim; ++tilex) {
            tile_t& tile = ind[tilemap[tiles[tiley][tilex]]];
            for (int y = 0; y < 10; ++y) {
                for (int x = 0; x < 10; ++x) {
                    if (x > 0 && y > 0 && x < 9 && y < 9) {
                        image[tiley*8+y-1][tilex*8+x-1] = get_tile_pix(tile, x, y);
                    } else {
                        if (x == 0 && tilex > 0) {
                            tile_t& p_tile = ind[tilemap[tiles[tiley][tilex-1]]];
                            assert(get_tile_pix(p_tile, 9, y) == get_tile_pix(tile, x, y));
                        }
                        if (y == 0 && tiley > 0) {
                            tile_t& p_tile = ind[tilemap[tiles[tiley-1][tilex]]];
                            assert(get_tile_pix(p_tile, x, 9) == get_tile_pix(tile, x, y));
                        }
                    }
                }
            }
        }
    }

    print_image(image, dim);
    //image = flipx(image);
    for (int i = 0; i < 4; ++i) {
        int seamonsters = count_seamonsters(image);
        if (seamonsters > 0) {
            print_image(image, dim);
        }
        std::cout << "Seamonsters: " << seamonsters << std::endl;
        image = rot(image);
    }
    image = flipy(image);
    for (int i = 0; i < 4; ++i) {
        int seamonsters = count_seamonsters(image);
        if (seamonsters > 0) {
            print_image(image, dim);
        }
        std::cout << "Seamonsters: " << seamonsters << std::endl;
        image = rot(image);
    }

    return value;
}

int main(int argc, char** argv) {
    auto indata = parse("input");
    // 2861 too high
    // 2831 too high
    // 2801 too high
    // 2846 not right
    std::cout << part1(indata) << std::endl;
    return 0;
}
