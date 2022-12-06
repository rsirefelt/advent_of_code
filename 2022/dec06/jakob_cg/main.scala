import scala.io.Source._

def findUnique(input: String, offset: Int): Int = 
    var done = false
    var i = 0
    while (i < input.length && !done)
        val chars = input.slice(i, i+offset)
        if chars.toSet.size == offset then
            done = true
        else
            i += 1
    i+offset

def part1(input: String) = 
    findUnique(input, 4)

def part2(input: String) = 
    findUnique(input, 14)

@main def main() = 
    val input = fromFile("input").getLines.toList(0)
    println(part1(input))
    println(part2(input))