const std = @import("std");

const IndataType = std.ArrayList(u32);

fn parse(file_name: []const u8, alloc_in: *std.mem.Allocator) !IndataType {
    var file = try std.fs.cwd().openFile(file_name, .{});
    defer file.close();

    var buf: [32]u8 = undefined;

    var list = IndataType.init(alloc_in);

    while (try file.reader().readUntilDelimiterOrEof(&buf, '\n')) |line| {
        var it = std.mem.tokenize(line, " \r");
        var v = try std.fmt.parseInt(u32, it.next().?, 2);
        try list.append(v);
    }
    return list;
}

fn part1(indata: IndataType) i32 {
    var counts = std.mem.zeroes([12] i32);

    for (indata.items) |v| {
        for (counts) |_, i| {
            counts[i] += (std.math.shr(i32, @intCast(i32, v), i) & 1) * 2 - 1;
        }
    }

    var gamma: i32 = 0;
    var epsilon: i32 = 0;
    for (counts) |count, i| {
        if (count > 0) {
            gamma += std.math.shl(i32, 1, i);
        } else {
            epsilon += std.math.shl(i32, 1, i);
        }
    }

    return gamma * epsilon;
}

fn countOnes(indata: IndataType, enabled: std.ArrayList(bool), bit: i32) i32 {
    var count: i32 = 0;
    for (indata.items) | v, i | {
        if (enabled.items[i]) {
            count += (std.math.shr(i32, @intCast(i32, v), bit) & 1) * 2 - 1;
        }
    }
    return count;
}

fn part2Sub(indata: IndataType, oxygen: bool, alloc: *std.mem.Allocator) !u32 {
    var enabled = std.ArrayList(bool).init(alloc);
    defer enabled.deinit();

    try enabled.resize(indata.items.len);
    for (enabled.items) |_, i| {
        enabled.items[i] = true;
    }

    var bit: i32 = 11;
    var removed: u32 = 0;
    while (bit >= 0) {
        var keep_ones = countOnes(indata, enabled, bit) >= 0;
        if (!oxygen) {
            keep_ones = !keep_ones;
        }
        for (indata.items) | v, i | {
            if (enabled.items[i]) {
                const is_one = std.math.shr(u32, v, bit) & 1 == 1;
                if (keep_ones != is_one) {
                    enabled.items[i] = false;
                    removed += 1;
                }
            }
        }
        if (indata.items.len - removed == 1) {
            break;
        }
        bit -= 1;
    }
    for (enabled.items) | e, i | {
        if (e) {
            return indata.items[i];
        }
    }
    unreachable;
}

fn part2(indata: IndataType, alloc: *std.mem.Allocator) !u32 {
    const oxygen = try part2Sub(indata, true, alloc);
    const co2 = try part2Sub(indata, false, alloc);
    return oxygen * co2;
}

pub fn main() anyerror!void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = &arena.allocator;

    var in_data = try parse("input.txt", alloc);
    std.log.info("part 1: {d}", .{part1(in_data)});
    std.log.info("part 2: {d}", .{part2(in_data, alloc)});
}
