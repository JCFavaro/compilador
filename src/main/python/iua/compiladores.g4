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
TRUE: 'true';
FALSE: 'false';
INCREMENTO: '++';
DECREMENTO: '--';

//Comparadores
IGUAL: '==';
DISTINTO: '!=';
MENOR: '<';
MENORIGUAL: '<=';
MAYOR: '>';
MAYORIGUAL: '>=';


//Tipo de datos
INT: 'int';
FLOAT: 'float';
STRING: 'string';
DOUBLE: 'double';
CHAR: 'char';

//Estructuras de control
IF: 'if';
FOR: 'for';
WHILE: 'while';

//Funciones
RETURN: 'return';

NUMERO: DIGITO+;

ID: (LETRA | '_') (LETRA | DIGITO | '_')*;

WS: [ \t\n\r] -> skip;

OTRO: .;

prog: instrucciones EOF;

instrucciones: 	instruccion instrucciones 				
				|
				;

instruccion:
	bloque
	| declaracion PYC
	| asignacion PYC	
	| deffuncion
	| decfuncion bloque
	| llamadafuncion
	| bloqueif
	| bloquefor
	| bloquewhile; 

bloque: LLA instrucciones LLC;

declaracion:
	tdato ID
	| tdato ID COMA	ID
	| tdato ID COMA	ID declaracion
	| ID COMA declaracion// hay que ver esto es el caso int a,b,c,d;  	
	| ID
	| tdato asignacion 
	| tdato asignacion COMA declaracion
	| asignacion COMA declaracion
	| asignacion;

asignacion: ID ASSIG NUMERO | ID ASSIG ID | ID ASSIG oparit;

tdato: INT | FLOAT | STRING | DOUBLE | CHAR;

oprelacionales: IGUAL 
				| DISTINTO
				| MENOR
				| MAYOR
				| AND
				| OR
				;

comparacion: ID oprelacionales NUMERO
			| NUMERO oprelacionales ID
			| ID oprelacionales ID
			| ID
			| FALSE
			| TRUE
			;

condicionFor: PA tdato asignacion PYC comparacion PYC ID INCREMENTO PC
			| PA tdato asignacion PYC comparacion PYC INCREMENTO ID PC;

condicion: PA comparacion PC
		;			

bloqueif : IF condicion bloque	
			| IF (condicion (AND|OR) condicion)*
			;

bloquewhile : WHILE condicion bloque
			;

bloquefor: FOR condicionFor bloque
		 ;

//operacion aritmetica logica opal

itop: 	oparit itop 
		| EOF
		;

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

//Funciones
decfuncion: tdato ID PA (ID | NUMERO | TRUE | FALSE | COMA)* PC
			| tdato ID PA ((ID | NUMERO | TRUE | FALSE)+ COMA (ID | NUMERO | TRUE | FALSE)+)* PC;

deffuncion: tdato ID PA (ID | tdato ID | NUMERO)* PC PYC
			| tdato ID PA ((ID | tdato ID | NUMERO)+ COMA (ID | tdato ID | NUMERO)+)* PC PYC; //Definicion, prototipo

llamadafuncion: ID PA (ID | tdato ID | NUMERO | COMA)* PC PYC
				| ID PA ((ID | tdato ID | NUMERO | COMA)+ COMA (ID | tdato ID | NUMERO | COMA)+)* PC PYC;