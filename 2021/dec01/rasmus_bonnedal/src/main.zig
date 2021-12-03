const std = @import("std");

fn parse(file_name: []const u8, alloc_in: *std.mem.Allocator) !std.ArrayList(i32) {
    var file = try std.fs.cwd().openFile(file_name, .{});
    defer file.close();

    var buf: [32]u8 = undefined;

    var list = std.ArrayList(i32).init(alloc_in);

    while (try file.reader().readUntilDelimiterOrEof(&buf, '\n')) |line| {
        var v = try std.fmt.parseInt(i32, line, 10);
        try list.append(v);
    }
    return list;
}

fn part01(in_data: std.ArrayList(i32)) i32 {
    var prev: i32 = undefined;
    var count: i32 = 0;
    for (in_data.items) |v, idx| {
        if (idx > 0 and v > prev) {
            count += 1;
        }
        prev = v;
    }
    return count;
}

pub fn part02(in_data: std.ArrayList(i32), alloc_in: *std.mem.Allocator) !i32 {
    var sliding_window_sum = std.ArrayList(i32).init(alloc_in);
    defer sliding_window_sum.deinit();

    try sliding_window_sum.append(0);
    try sliding_window_sum.append(0);
    var i: u32 = 0;

    for (in_data.items) |v, idx| {
        sliding_window_sum.items[idx] += v;
        sliding_window_sum.items[idx + 1] += v;
        try sliding_window_sum.append(v);
    }

    var prev: i32 = sliding_window_sum.items[2];
    var count: i32 = 0;
    const len = sliding_window_sum.items.len;
    for (sliding_window_sum.items[3 .. len - 2]) |x, idx| {
        if (x > prev) {
            count += 1;
        }
        prev = x;
    }
    return count;
}

pub fn main() anyerror!void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = &arena.allocator;

    var in_data = try parse("input1.txt", alloc);

    std.log.info("part 1: {d}", .{part01(in_data)});
    std.log.info("part 2: {d}", .{part02(in_data, alloc)});
}
