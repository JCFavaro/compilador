grammar compiladores;

fragment LETRA: [A-Za-z];
fragment DIGITO: [0-9];

//Operadores
PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
PYC: ';';
COMA: ',';

//Operaciones aritmeticas
MULT: '*';
DIV: '/';
SUMA: '+';
RESTA: '-';
MOD: '%';

//Operaciones logicas
AND: '&&';
OR: '||';
NOT: '!';
ASSIG: '=';

//Comparadores
IGUAL: '==';
DISTINTO: '!=';
MENOR: '<';
MAYOR: '>';

//Tipo de datos
INT: 'int';
FLOAT: 'float';
STRING: 'string';
DOUBLE: 'double';

//Estructuras de control
IF: 'if';
FOR: 'for';
WHILE: 'while';

//Funciones

NUMERO: DIGITO+;

ID: (LETRA | '_') (LETRA | DIGITO | '_')*;

WS: [ \t\n\r] -> skip;

OTRO: .;

prog: instrucciones EOF;

instrucciones: instruccion instrucciones |;

instruccion:
	bloque PYC
	| declaracion PYC
	| asignacion PYC; // | bloqueif | bloquefor | bloquewhile

bloque: LLA instrucciones LLC;

declaracion:
	tdato ID
	| tdato ID COMA declaracion
	| tdato asignacion
	| ID COMA declaracion // hay que ver esto es el caso int a,b,c,d;  
	| ID
	| asignacion
	| asignacion COMA declaracion;

asignacion: ID ASSIG NUMERO | ID ASSIG ID;

tdato: INT | FLOAT | STRING | DOUBLE;

// bloqueif : condicion bloque;

// condicion: PA comparacion PC;

// comparacion: ;

// bloquewhile : PA comparacion/opal PC instruccion;

//operacion aritmetica logica opal

itop: oparit itop | EOF;

oparitlog: predicado;

predicado: |;

oparit: exp;

exp: term t;

term: factor f;

t: 	SUMA term t 
	| RESTA term t 
	| OR term t 
	| factor
	|
	;

factor: ID 
		| NUMERO 
		| PA exp PC
		;

f: 	MULT factor f 
	| DIV factor f 
	| AND factor f 
	| MOD factor f 
	|
	;