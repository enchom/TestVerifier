grammar format;

format_file
    : FORMAT NEWLINE format_block NEWLINE* CONSTRAINTS NEWLINE constraints_block NEWLINE* EOF
    ;

format_block
    : ID (NEWLINE? ID)*
    ;

constraints_block
    : constraint (NEWLINE* constraint)* NEWLINE*
    ;

constraint
    : ID type                                                                           #type_constraint
    | ID binary_comparison_operator constant                                            #binary_operator_constraint
    | constant binary_comparison_operator ID binary_comparison_operator constant        #binary_chain_constraint
    ;

binary_comparison_operator: EQ | NEQ | LEQ | LESS | GEQ | GREATER;

type: INT | STRING | REAL;

constant: INT_CONSTANT | REAL_CONSTANT;

SPACE:              ' '                 -> skip;
TAB:                '\t'                -> skip;
NEWLINE:            '\r\n' | '\n';
EQ:                 '=';
LEQ:                '<=';
LESS:               '<';
GEQ:                '>=';
GREATER:            '>';
NEQ:                '!=' | '<>';

FORMAT:             'FORMAT';
CONSTRAINTS:        'CONSTRAINTS';
INT:                'INT';
STRING:             'STRING';
REAL:               'REAL';

ID:                 [a-zA-Z][a-zA-Z0-9]*;
INT_CONSTANT:       [0-9]+;
REAL_CONSTANT:      [0-9]+ ('.' [0-9]+)?;
