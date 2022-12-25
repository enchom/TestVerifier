from pathlib import Path

from antlr4 import InputStream, CommonTokenStream

from grammar.generated.formatLexer import formatLexer
from verifier.grammar.generated.formatParser import formatParser


def parse_format(file: Path):
    format_data = file.read_text(encoding="UTF-8")

    lexer = formatLexer(InputStream(data=format_data))
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    for token in token_stream.tokens:
        print(token)

    parser = formatParser(token_stream)
    format_file = parser.format_file()


if __name__ == "__main__":
    FILE = Path(r"D:\Programs\TestVerifier\examples\IATI_2022_E2.txt")
    parse_format(FILE)