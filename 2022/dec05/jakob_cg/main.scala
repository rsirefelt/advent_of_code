import scala.io.Source._
import scala.util.matching.Regex

var testlist = List(
    List("Z", "N"),
    List("M", "C", "D"),
    List("P")
)

var realList = List(
    List("B", "P", "N", "Q", "H", "D", "R", "T"),
    List("W", "G", "B", "J", "T", "V"),
    List("N", "R", "H", "D", "S", "V", "M", "Q"),
    List("P", "Z", "N", "M", "C"),
    List("D", "Z", "B"),
    List("V", "C", "W", "Z"),
    List("G", "Z", "N", "C", "V", "Q", "L", "S"),
    List("L", "G", "J", "M", "D", "N", "V"),
    List("T", "P", "M", "F", "Z", "C", "G"),
)

def part1(input: List[String]) =
    val pattern: Regex = """move (\d+) from (\d+) to (\d+)""".r
    var list = realList
    for line <- input do
        val patternMatch = pattern.findAllMatchIn(line).toList(0)
        val amount = patternMatch.group(1).toString.toInt
        var fromIndex = patternMatch.group(2).toString.toInt - 1
        var toIndex = patternMatch.group(3).toString.toInt - 1
        val cratesToMove = list(fromIndex).takeRight(amount)
        list = list.updated(fromIndex, list(fromIndex).dropRight(amount))
        list = list.updated(toIndex, list(toIndex) ++ cratesToMove.reverse)

    var result = ""
    for stack <- list do
        result += stack.last
    
    result

def part2(input: List[String]) =
    val pattern: Regex = """move (\d+) from (\d+) to (\d+)""".r
    var list = realList
    for line <- input do
        val patternMatch = pattern.findAllMatchIn(line).toList(0)
        val amount = patternMatch.group(1).toString.toInt
        var fromIndex = patternMatch.group(2).toString.toInt - 1
        var toIndex = patternMatch.group(3).toString.toInt - 1
        val cratesToMove = list(fromIndex).takeRight(amount)
        list = list.updated(fromIndex, list(fromIndex).dropRight(amount))
        list = list.updated(toIndex, list(toIndex) ++ cratesToMove)

    var result = ""
    for stack <- list do
        result += stack.last
    
    result

@main def main() =
    val input = fromFile("input").getLines.toList
    println(part1(input))
    println(part2(input))