# Generated from format.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .formatParser import formatParser
else:
    from formatParser import formatParser

# This class defines a complete listener for a parse tree produced by formatParser.
class formatListener(ParseTreeListener):

    # Enter a parse tree produced by formatParser#format_file.
    def enterFormat_file(self, ctx:formatParser.Format_fileContext):
        pass

    # Exit a parse tree produced by formatParser#format_file.
    def exitFormat_file(self, ctx:formatParser.Format_fileContext):
        pass


    # Enter a parse tree produced by formatParser#format_block.
    def enterFormat_block(self, ctx:formatParser.Format_blockContext):
        pass

    # Exit a parse tree produced by formatParser#format_block.
    def exitFormat_block(self, ctx:formatParser.Format_blockContext):
        pass


    # Enter a parse tree produced by formatParser#constraints_block.
    def enterConstraints_block(self, ctx:formatParser.Constraints_blockContext):
        pass

    # Exit a parse tree produced by formatParser#constraints_block.
    def exitConstraints_block(self, ctx:formatParser.Constraints_blockContext):
        pass


    # Enter a parse tree produced by formatParser#type_constraint.
    def enterType_constraint(self, ctx:formatParser.Type_constraintContext):
        pass

    # Exit a parse tree produced by formatParser#type_constraint.
    def exitType_constraint(self, ctx:formatParser.Type_constraintContext):
        pass


    # Enter a parse tree produced by formatParser#binary_operator_constraint.
    def enterBinary_operator_constraint(self, ctx:formatParser.Binary_operator_constraintContext):
        pass

    # Exit a parse tree produced by formatParser#binary_operator_constraint.
    def exitBinary_operator_constraint(self, ctx:formatParser.Binary_operator_constraintContext):
        pass


    # Enter a parse tree produced by formatParser#binary_chain_constraint.
    def enterBinary_chain_constraint(self, ctx:formatParser.Binary_chain_constraintContext):
        pass

    # Exit a parse tree produced by formatParser#binary_chain_constraint.
    def exitBinary_chain_constraint(self, ctx:formatParser.Binary_chain_constraintContext):
        pass


    # Enter a parse tree produced by formatParser#binary_comparison_operator.
    def enterBinary_comparison_operator(self, ctx:formatParser.Binary_comparison_operatorContext):
        pass

    # Exit a parse tree produced by formatParser#binary_comparison_operator.
    def exitBinary_comparison_operator(self, ctx:formatParser.Binary_comparison_operatorContext):
        pass


    # Enter a parse tree produced by formatParser#type.
    def enterType(self, ctx:formatParser.TypeContext):
        pass

    # Exit a parse tree produced by formatParser#type.
    def exitType(self, ctx:formatParser.TypeContext):
        pass


    # Enter a parse tree produced by formatParser#constant.
    def enterConstant(self, ctx:formatParser.ConstantContext):
        pass

    # Exit a parse tree produced by formatParser#constant.
    def exitConstant(self, ctx:formatParser.ConstantContext):
        pass



del formatParser