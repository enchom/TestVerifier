# Generated from format.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,84,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,5,0,19,8,0,10,0,12,0,22,9,0,1,0,1,0,1,0,1,0,5,
        0,28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,3,1,37,8,1,1,1,5,1,40,
        8,1,10,1,12,1,43,9,1,1,2,1,2,5,2,47,8,2,10,2,12,2,50,9,2,1,2,5,2,
        53,8,2,10,2,12,2,56,9,2,1,2,5,2,59,8,2,10,2,12,2,62,9,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,76,8,3,1,4,1,4,1,5,1,
        5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,3,1,0,4,9,1,0,12,14,1,0,16,
        17,85,0,14,1,0,0,0,2,34,1,0,0,0,4,44,1,0,0,0,6,75,1,0,0,0,8,77,1,
        0,0,0,10,79,1,0,0,0,12,81,1,0,0,0,14,15,5,10,0,0,15,16,5,3,0,0,16,
        20,3,2,1,0,17,19,5,3,0,0,18,17,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,
        0,20,21,1,0,0,0,21,23,1,0,0,0,22,20,1,0,0,0,23,24,5,11,0,0,24,25,
        5,3,0,0,25,29,3,4,2,0,26,28,5,3,0,0,27,26,1,0,0,0,28,31,1,0,0,0,
        29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,
        0,0,1,33,1,1,0,0,0,34,41,5,15,0,0,35,37,5,3,0,0,36,35,1,0,0,0,36,
        37,1,0,0,0,37,38,1,0,0,0,38,40,5,15,0,0,39,36,1,0,0,0,40,43,1,0,
        0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,41,1,0,0,0,44,54,
        3,6,3,0,45,47,5,3,0,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,
        48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,53,3,6,3,0,52,48,1,
        0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,60,1,0,0,0,56,
        54,1,0,0,0,57,59,5,3,0,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,
        0,60,61,1,0,0,0,61,5,1,0,0,0,62,60,1,0,0,0,63,64,5,15,0,0,64,76,
        3,10,5,0,65,66,5,15,0,0,66,67,3,8,4,0,67,68,3,12,6,0,68,76,1,0,0,
        0,69,70,3,12,6,0,70,71,3,8,4,0,71,72,5,15,0,0,72,73,3,8,4,0,73,74,
        3,12,6,0,74,76,1,0,0,0,75,63,1,0,0,0,75,65,1,0,0,0,75,69,1,0,0,0,
        76,7,1,0,0,0,77,78,7,0,0,0,78,9,1,0,0,0,79,80,7,1,0,0,80,11,1,0,
        0,0,81,82,7,2,0,0,82,13,1,0,0,0,8,20,29,36,41,48,54,60,75
    ]

class formatParser ( Parser ):

    grammarFileName = "format.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '", "'\\t'", "<INVALID>", "'='", "'<='", 
                     "'<'", "'>='", "'>'", "<INVALID>", "'FORMAT'", "'CONSTRAINTS'", 
                     "'INT'", "'STRING'", "'REAL'" ]

    symbolicNames = [ "<INVALID>", "SPACE", "TAB", "NEWLINE", "EQ", "LEQ", 
                      "LESS", "GEQ", "GREATER", "NEQ", "FORMAT", "CONSTRAINTS", 
                      "INT", "STRING", "REAL", "ID", "INT_CONSTANT", "REAL_CONSTANT" ]

    RULE_format_file = 0
    RULE_format_block = 1
    RULE_constraints_block = 2
    RULE_constraint = 3
    RULE_binary_comparison_operator = 4
    RULE_type = 5
    RULE_constant = 6

    ruleNames =  [ "format_file", "format_block", "constraints_block", "constraint", 
                   "binary_comparison_operator", "type", "constant" ]

    EOF = Token.EOF
    SPACE=1
    TAB=2
    NEWLINE=3
    EQ=4
    LEQ=5
    LESS=6
    GEQ=7
    GREATER=8
    NEQ=9
    FORMAT=10
    CONSTRAINTS=11
    INT=12
    STRING=13
    REAL=14
    ID=15
    INT_CONSTANT=16
    REAL_CONSTANT=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Format_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORMAT(self):
            return self.getToken(formatParser.FORMAT, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(formatParser.NEWLINE)
            else:
                return self.getToken(formatParser.NEWLINE, i)

        def format_block(self):
            return self.getTypedRuleContext(formatParser.Format_blockContext,0)


        def CONSTRAINTS(self):
            return self.getToken(formatParser.CONSTRAINTS, 0)

        def constraints_block(self):
            return self.getTypedRuleContext(formatParser.Constraints_blockContext,0)


        def EOF(self):
            return self.getToken(formatParser.EOF, 0)

        def getRuleIndex(self):
            return formatParser.RULE_format_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormat_file" ):
                listener.enterFormat_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormat_file" ):
                listener.exitFormat_file(self)




    def format_file(self):

        localctx = formatParser.Format_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_format_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(formatParser.FORMAT)
            self.state = 15
            self.match(formatParser.NEWLINE)
            self.state = 16
            self.format_block()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 17
                self.match(formatParser.NEWLINE)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
            self.match(formatParser.CONSTRAINTS)
            self.state = 24
            self.match(formatParser.NEWLINE)
            self.state = 25
            self.constraints_block()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 26
                self.match(formatParser.NEWLINE)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(formatParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Format_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(formatParser.ID)
            else:
                return self.getToken(formatParser.ID, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(formatParser.NEWLINE)
            else:
                return self.getToken(formatParser.NEWLINE, i)

        def getRuleIndex(self):
            return formatParser.RULE_format_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormat_block" ):
                listener.enterFormat_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormat_block" ):
                listener.exitFormat_block(self)




    def format_block(self):

        localctx = formatParser.Format_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_format_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(formatParser.ID)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==3:
                        self.state = 35
                        self.match(formatParser.NEWLINE)


                    self.state = 38
                    self.match(formatParser.ID) 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constraints_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(formatParser.ConstraintContext)
            else:
                return self.getTypedRuleContext(formatParser.ConstraintContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(formatParser.NEWLINE)
            else:
                return self.getToken(formatParser.NEWLINE, i)

        def getRuleIndex(self):
            return formatParser.RULE_constraints_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraints_block" ):
                listener.enterConstraints_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraints_block" ):
                listener.exitConstraints_block(self)




    def constraints_block(self):

        localctx = formatParser.Constraints_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constraints_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.constraint()
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 48
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==3:
                        self.state = 45
                        self.match(formatParser.NEWLINE)
                        self.state = 50
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 51
                    self.constraint() 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self.match(formatParser.NEWLINE) 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return formatParser.RULE_constraint

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Binary_operator_constraintContext(ConstraintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a formatParser.ConstraintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(formatParser.ID, 0)
        def binary_comparison_operator(self):
            return self.getTypedRuleContext(formatParser.Binary_comparison_operatorContext,0)

        def constant(self):
            return self.getTypedRuleContext(formatParser.ConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_operator_constraint" ):
                listener.enterBinary_operator_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_operator_constraint" ):
                listener.exitBinary_operator_constraint(self)


    class Binary_chain_constraintContext(ConstraintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a formatParser.ConstraintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(formatParser.ConstantContext)
            else:
                return self.getTypedRuleContext(formatParser.ConstantContext,i)

        def binary_comparison_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(formatParser.Binary_comparison_operatorContext)
            else:
                return self.getTypedRuleContext(formatParser.Binary_comparison_operatorContext,i)

        def ID(self):
            return self.getToken(formatParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_chain_constraint" ):
                listener.enterBinary_chain_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_chain_constraint" ):
                listener.exitBinary_chain_constraint(self)


    class Type_constraintContext(ConstraintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a formatParser.ConstraintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(formatParser.ID, 0)
        def type_(self):
            return self.getTypedRuleContext(formatParser.TypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_constraint" ):
                listener.enterType_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_constraint" ):
                listener.exitType_constraint(self)



    def constraint(self):

        localctx = formatParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constraint)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = formatParser.Type_constraintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(formatParser.ID)
                self.state = 64
                self.type_()
                pass

            elif la_ == 2:
                localctx = formatParser.Binary_operator_constraintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(formatParser.ID)
                self.state = 66
                self.binary_comparison_operator()
                self.state = 67
                self.constant()
                pass

            elif la_ == 3:
                localctx = formatParser.Binary_chain_constraintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.constant()
                self.state = 70
                self.binary_comparison_operator()
                self.state = 71
                self.match(formatParser.ID)
                self.state = 72
                self.binary_comparison_operator()
                self.state = 73
                self.constant()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_comparison_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(formatParser.EQ, 0)

        def NEQ(self):
            return self.getToken(formatParser.NEQ, 0)

        def LEQ(self):
            return self.getToken(formatParser.LEQ, 0)

        def LESS(self):
            return self.getToken(formatParser.LESS, 0)

        def GEQ(self):
            return self.getToken(formatParser.GEQ, 0)

        def GREATER(self):
            return self.getToken(formatParser.GREATER, 0)

        def getRuleIndex(self):
            return formatParser.RULE_binary_comparison_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_comparison_operator" ):
                listener.enterBinary_comparison_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_comparison_operator" ):
                listener.exitBinary_comparison_operator(self)




    def binary_comparison_operator(self):

        localctx = formatParser.Binary_comparison_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_binary_comparison_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(formatParser.INT, 0)

        def STRING(self):
            return self.getToken(formatParser.STRING, 0)

        def REAL(self):
            return self.getToken(formatParser.REAL, 0)

        def getRuleIndex(self):
            return formatParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = formatParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_CONSTANT(self):
            return self.getToken(formatParser.INT_CONSTANT, 0)

        def REAL_CONSTANT(self):
            return self.getToken(formatParser.REAL_CONSTANT, 0)

        def getRuleIndex(self):
            return formatParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = formatParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





