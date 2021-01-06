/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    AND = 258,
    OR = 259,
    NOT = 260,
    IF = 261,
    ELSE = 262,
    ELIF = 263,
    WHILE = 264,
    FOR = 265,
    READ = 266,
    WRITE = 267,
    INTEGER = 268,
    STRING = 269,
    CHAR = 270,
    BOOL = 271,
    RETURN = 272,
    PROGRAM = 273,
    IDENTIFIER = 274,
    CONSTANT = 275,
    SEMI_COLON = 276,
    COMMA = 277,
    DOT = 278,
    OPEN_CURLY_BRACKET = 279,
    CLOSED_CURLY_BRACKET = 280,
    OPEN_SQUARE_BRACKET = 281,
    CLOSED_SQUARE_BRACKET = 282,
    OPEN_ROUND_BRACKET = 283,
    CLOSED_ROUND_BRACKET = 284,
    PLUS = 285,
    MINUS = 286,
    MUL = 287,
    DIV = 288,
    PERCENT = 289,
    LT = 290,
    GT = 291,
    LE = 292,
    GE = 293,
    ATRIB = 294,
    EQ = 295,
    NOT_EQ = 296
  };
#endif
/* Tokens.  */
#define AND 258
#define OR 259
#define NOT 260
#define IF 261
#define ELSE 262
#define ELIF 263
#define WHILE 264
#define FOR 265
#define READ 266
#define WRITE 267
#define INTEGER 268
#define STRING 269
#define CHAR 270
#define BOOL 271
#define RETURN 272
#define PROGRAM 273
#define IDENTIFIER 274
#define CONSTANT 275
#define SEMI_COLON 276
#define COMMA 277
#define DOT 278
#define OPEN_CURLY_BRACKET 279
#define CLOSED_CURLY_BRACKET 280
#define OPEN_SQUARE_BRACKET 281
#define CLOSED_SQUARE_BRACKET 282
#define OPEN_ROUND_BRACKET 283
#define CLOSED_ROUND_BRACKET 284
#define PLUS 285
#define MINUS 286
#define MUL 287
#define DIV 288
#define PERCENT 289
#define LT 290
#define GT 291
#define LE 292
#define GE 293
#define ATRIB 294
#define EQ 295
#define NOT_EQ 296

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
