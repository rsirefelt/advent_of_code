const std = @import("std");

const Direction = enum {
    forward,
    up,
    down,

    pub fn fromString(s: []const u8) Direction {
        if (std.mem.eql(u8, s, "forward")) {
            return Direction.forward;
        } else if (std.mem.eql(u8, s, "up")) {
            return Direction.up;
        } else if (std.mem.eql(u8, s, "down")) {
            return Direction.down;
        }
        unreachable;
    }
};

const StringInt = struct { direction: Direction, length: i32 };

fn parse(file_name: []const u8, alloc_in: *std.mem.Allocator) !std.ArrayList(StringInt) {
    var file = try std.fs.cwd().openFile(file_name, .{});
    defer file.close();

    var buf: [32]u8 = undefined;

    var list = std.ArrayList(StringInt).init(alloc_in);

    while (try file.reader().readUntilDelimiterOrEof(&buf, '\n')) |line| {
        var it = std.mem.tokenize(line, " \r");
        var direction = Direction.fromString(it.next().?);
        var v = try std.fmt.parseInt(i32, it.next().?, 10);
        try list.append(.{ .direction = direction, .length = v });
    }
    return list;
}

fn part1(indata: std.ArrayList(StringInt)) i32 {
    var horizontal: i32 = 0;
    var depth: i32 = 0;
    for (indata.items) |entry| {
        switch(entry.direction) {
            .forward => horizontal += entry.length,
            .up => depth -= entry.length,
            .down => depth += entry.length,
        }
    }
    return horizontal * depth;
}

fn part2(indata: std.ArrayList(StringInt)) i32 {
    var horizontal: i32 = 0;
    var depth: i32 = 0;
    var aim: i32 = 0;
    for (indata.items) |entry| {
        switch(entry.direction) {
            .forward => {
                horizontal += entry.length;
                depth += aim * entry.length;
            },
            .up => aim -= entry.length,
            .down => aim += entry.length,
        }
    }
    return horizontal * depth;
}


pub fn main() anyerror!void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = &arena.allocator;

    var in_data = try parse("input.txt", alloc);
    std.log.info("part 1: {d}", .{part1(in_data)});
    std.log.info("part 2: {d}", .{part2(in_data)});
}
