/*==============================================================*/
/* DBMS name:      ORACLE Version 11g                           */
/* Created on:     19/07/2022 02:43:26 p. m.                    */
/*==============================================================*/

alter table ASISTENCIA
   drop constraint FK_ASISTENC_ESTUDIANT_ESTUDIAN;

alter table ASISTENCIA
   drop constraint FK_ASISTENC_PRACTICA_PRACTICA;

alter table DEPORTE
   drop constraint FK_DEPORTE_MATERIALE_MATERIAL;

alter table ESPACIO
   drop constraint FK_ESPACIO_HORARIOS_HORARIO;

alter table ESPACIO
   drop constraint FK_ESPACIO_SEDEESPAC_SEDE;

alter table ESTUDIANTE
   drop constraint FK_ESTUDIAN_PASANTE_ROL;

alter table HISTORICO
   drop constraint FK_HISTORIC_HISTORICO_PRACTICA;

alter table HORARIO
   drop constraint FK_HORARIO_DIAS_DIA;

alter table HORARIO
   drop constraint FK_HORARIO_HORAS_HORA;

alter table INSTRUCTOR
   drop constraint FK_INSTRUCT_PROFESORO_SEDE;

alter table INSTRUCTOR
   drop constraint FK_INSTRUCT_TIPOINSTR_ROL;

alter table MATERIAL
   drop constraint FK_MATERIAL_ESTADOMAT_ESTADO;

alter table PERSONAL
   drop constraint FK_PERSONAL_EMPLEADOS_SEDE;

alter table PERSONAL
   drop constraint FK_PERSONAL_PERSONAL_ROL;

alter table PRACTICA
   drop constraint FK_PRACTICA_DEPORTEAP_DEPORTE;

alter table PRACTICA
   drop constraint FK_PRACTICA_ESPACIOAS_ESPACIO;

alter table PRACTICA
   drop constraint FK_PRACTICA_ESTADOPRA_ESTADO;

alter table PRACTICA
   drop constraint FK_PRACTICA_PASANTEPR_ESTUDIAN;

alter table PRACTICA
   drop constraint FK_PRACTICA_PROFESORE_INSTRUCT;

alter table PRACTICA
   drop constraint FK_PRACTICA_TIPOPRACT_TIPOPRAC;

drop index ESTUDIANTES_FK;

drop index PRACTICA_FK;

drop table ASISTENCIA cascade constraints;

drop index MATERIALESDEPORTE_FK;

drop table DEPORTE cascade constraints;

drop table DIA cascade constraints;

drop index HORARIOS_FK;

drop index SEDEESPACIO_FK;

drop table ESPACIO cascade constraints;

drop table ESTADO cascade constraints;

drop index PASANTE_FK;

drop table ESTUDIANTE cascade constraints;

drop index HISTORICOUSO_FK;

drop table HISTORICO cascade constraints;

drop table HORA cascade constraints;

drop index HORAS_FK;

drop index DIAS_FK;

drop table HORARIO cascade constraints;

drop index PROFESOROINSTRUCTOR_FK;

drop index TIPOINSTRUCTOR_FK;

drop table INSTRUCTOR cascade constraints;

drop index ESTADOMATERIALES_FK;

drop table MATERIAL cascade constraints;

drop index EMPLEADOS_FK;

drop index PERSONAL_FK;

drop table PERSONAL cascade constraints;

drop index ESPACIOASIGNADO_FK;

drop index PROFESORENTRENADOR_FK;

drop index PASANTEPRACTICA2_FK;

drop index DEPORTEAPRACTICAR_FK;

drop index ESTADOPRACTICA_FK;

drop index TIPOPRACTICA_FK;

drop table PRACTICA cascade constraints;

drop table ROL cascade constraints;

drop table SEDE cascade constraints;

drop table TIPOPRACTICAS cascade constraints;

/*==============================================================*/
/* Table: ASISTENCIA                                            */
/*==============================================================*/
create table ASISTENCIA 
(
   IDASISTENCIA         VARCHAR2(8)          not null,
   IDESPACIOFK          VARCHAR2(10)         not null,
   IDPRACTICAFK         VARCHAR2(10)         not null,
   IDESTUDIANTEFK       VARCHAR2(10)         not null,
   constraint PK_ASISTENCIA primary key (IDASISTENCIA)
);

/*==============================================================*/
/* Index: PRACTICA_FK                                           */
/*==============================================================*/
create index PRACTICA_FK on ASISTENCIA (
   IDESPACIOFK ASC,
   IDPRACTICAFK ASC
);

/*==============================================================*/
/* Index: ESTUDIANTES_FK                                        */
/*==============================================================*/
create index ESTUDIANTES_FK on ASISTENCIA (
   IDESTUDIANTEFK ASC
);

/*==============================================================*/
/* Table: DEPORTE                                               */
/*==============================================================*/
create table DEPORTE 
(
   IDDEPORTE            VARCHAR2(10)         not null,
   IDMATERIALFK         VARCHAR2(10)         not null,
   DESCDEPORTE          VARCHAR2(30)         not null,
   constraint PK_DEPORTE primary key (IDDEPORTE)
);

/*==============================================================*/
/* Index: MATERIALESDEPORTE_FK                                  */
/*==============================================================*/
create index MATERIALESDEPORTE_FK on DEPORTE (
   IDMATERIALFK ASC
);

/*==============================================================*/
/* Table: DIA                                                   */
/*==============================================================*/
create table DIA 
(
   IDDIA                NUMBER(1,0)          not null,
   DESCDIA              VARCHAR2(10)         not null,
   constraint PK_DIA primary key (IDDIA)
);

/*==============================================================*/
/* Table: ESPACIO                                               */
/*==============================================================*/
create table ESPACIO 
(
   IDESPACIO            VARCHAR2(10)         not null,
   IDHORARIOFK          VARCHAR2(10)         not null,
   IDSEDEFK             VARCHAR2(10)         not null,
   DESCESPACIO          VARCHAR2(30)         not null,
   constraint PK_ESPACIO primary key (IDESPACIO)
);

/*==============================================================*/
/* Index: SEDEESPACIO_FK                                        */
/*==============================================================*/
create index SEDEESPACIO_FK on ESPACIO (
   IDSEDEFK ASC
);

/*==============================================================*/
/* Index: HORARIOS_FK                                           */
/*==============================================================*/
create index HORARIOS_FK on ESPACIO (
   IDHORARIOFK ASC
);

/*==============================================================*/
/* Table: ESTADO                                                */
/*==============================================================*/
create table ESTADO 
(
   IDESTADO             VARCHAR2(10)         not null,
   DESCESTADO           VARCHAR2(30)         not null,
   constraint PK_ESTADO primary key (IDESTADO)
);

/*==============================================================*/
/* Table: ESTUDIANTE                                            */
/*==============================================================*/
create table ESTUDIANTE 
(
   IDESTUDIANTE         VARCHAR2(10)         not null,
   IDROLFK              VARCHAR2(10),
   NOMBREESTUDIANTE     VARCHAR2(20)         not null,
   APELLIDOESTUDIANTE   VARCHAR2(30)         not null,
   constraint PK_ESTUDIANTE primary key (IDESTUDIANTE)
);

/*==============================================================*/
/* Index: PASANTE_FK                                            */
/*==============================================================*/
create index PASANTE_FK on ESTUDIANTE (
   IDROLFK ASC
);

/*==============================================================*/
/* Table: HISTORICO                                             */
/*==============================================================*/
create table HISTORICO 
(
   IDHISTORIA           VARCHAR2(10)         not null,
   IDESPACIOFK          VARCHAR2(10)         not null,
   IDPRACTICAFK         VARCHAR2(10)         not null,
   FECHAREGISTRO        DATE                 not null,
   HORAINI              DATE                 not null,
   HORAFIN              DATE                 not null,
   constraint PK_HISTORICO primary key (IDHISTORIA)
);

/*==============================================================*/
/* Index: HISTORICOUSO_FK                                       */
/*==============================================================*/
create index HISTORICOUSO_FK on HISTORICO (
   IDESPACIOFK ASC,
   IDPRACTICAFK ASC
);

/*==============================================================*/
/* Table: HORA                                                  */
/*==============================================================*/
create table HORA 
(
   IDHORA               VARCHAR2(10)         not null,
   HORAINICIO           DATE                 not null,
   HORAFIN              DATE                 not null,
   constraint PK_HORA primary key (IDHORA)
);

/*==============================================================*/
/* Table: HORARIO                                               */
/*==============================================================*/
create table HORARIO 
(
   IDHORARIO            VARCHAR2(10)         not null,
   IDHORAFK             VARCHAR2(10)         not null,
   IDDIAFK              NUMBER(1,0)          not null,
   constraint PK_HORARIO primary key (IDHORARIO)
);

/*==============================================================*/
/* Index: DIAS_FK                                               */
/*==============================================================*/
create index DIAS_FK on HORARIO (
   IDDIAFK ASC
);

/*==============================================================*/
/* Index: HORAS_FK                                              */
/*==============================================================*/
create index HORAS_FK on HORARIO (
   IDHORAFK ASC
);

/*==============================================================*/
/* Table: INSTRUCTOR                                            */
/*==============================================================*/
create table INSTRUCTOR 
(
   IDDOCENTE            VARCHAR2(10)         not null,
   IDROLFK              VARCHAR2(10)         not null,
   IDSEDEFK             VARCHAR2(10)         not null,
   NOMBREDOCENTE        VARCHAR2(30)         not null,
   APELLIDODOCENTE      VARCHAR2(30)         not null,
   constraint PK_INSTRUCTOR primary key (IDDOCENTE)
);

/*==============================================================*/
/* Index: TIPOINSTRUCTOR_FK                                     */
/*==============================================================*/
create index TIPOINSTRUCTOR_FK on INSTRUCTOR (
   IDROLFK ASC
);

/*==============================================================*/
/* Index: PROFESOROINSTRUCTOR_FK                                */
/*==============================================================*/
create index PROFESOROINSTRUCTOR_FK on INSTRUCTOR (
   IDSEDEFK ASC
);

/*==============================================================*/
/* Table: MATERIAL                                              */
/*==============================================================*/
create table MATERIAL 
(
   IDMATERIAL           VARCHAR2(10)         not null,
   IDESTADOFK           VARCHAR2(10)         not null,
   DESCMATERIAL         VARCHAR2(30)         not null,
   MARCAMATEIRAL        VARCHAR2(40)         not null,
   FECHACOMPRA          DATE                 not null,
   constraint PK_MATERIAL primary key (IDMATERIAL)
);

/*==============================================================*/
/* Index: ESTADOMATERIALES_FK                                   */
/*==============================================================*/
create index ESTADOMATERIALES_FK on MATERIAL (
   IDESTADOFK ASC
);

/*==============================================================*/
/* Table: PERSONAL                                              */
/*==============================================================*/
create table PERSONAL 
(
   IDPERSONAL           VARCHAR2(10)         not null,
   IDROLFK              VARCHAR2(10)         not null,
   IDSEDEFK             VARCHAR2(10)         not null,
   NOMBREDOCENTE        VARCHAR2(30)         not null,
   APELLIDODOCENTE      VARCHAR2(30)         not null,
   constraint PK_PERSONAL primary key (IDPERSONAL)
);

/*==============================================================*/
/* Index: PERSONAL_FK                                           */
/*==============================================================*/
create index PERSONAL_FK on PERSONAL (
   IDROLFK ASC
);

/*==============================================================*/
/* Index: EMPLEADOS_FK                                          */
/*==============================================================*/
create index EMPLEADOS_FK on PERSONAL (
   IDSEDEFK ASC
);

/*==============================================================*/
/* Table: PRACTICA                                              */
/*==============================================================*/
create table PRACTICA 
(
   IDESPACIOFK          VARCHAR2(10)         not null,
   IDPRACTICA           VARCHAR2(10)         not null,
   IDDEPORTEFK          VARCHAR2(10)         not null,
   IDTIPOPRACTICAFK     NUMBER(2)            not null,
   IDDOCENTEFK          VARCHAR2(10)         not null,
   IDESTADOFK           VARCHAR2(10)         not null,
   IDESTUDIANTEFK       VARCHAR2(10),
   DESCCURSO            VARCHAR2(50),
   CREDITOS             NUMBER(1,0)          not null,
   constraint PK_PRACTICA primary key (IDESPACIOFK, IDPRACTICA)
);

/*==============================================================*/
/* Index: TIPOPRACTICA_FK                                       */
/*==============================================================*/
create index TIPOPRACTICA_FK on PRACTICA (
   IDTIPOPRACTICAFK ASC
);

/*==============================================================*/
/* Index: ESTADOPRACTICA_FK                                     */
/*==============================================================*/
create index ESTADOPRACTICA_FK on PRACTICA (
   IDESTADOFK ASC
);

/*==============================================================*/
/* Index: DEPORTEAPRACTICAR_FK                                  */
/*==============================================================*/
create index DEPORTEAPRACTICAR_FK on PRACTICA (
   IDDEPORTEFK ASC
);

/*==============================================================*/
/* Index: PASANTEPRACTICA2_FK                                   */
/*==============================================================*/
create index PASANTEPRACTICA2_FK on PRACTICA (
   IDESTUDIANTEFK ASC
);

/*==============================================================*/
/* Index: PROFESORENTRENADOR_FK                                 */
/*==============================================================*/
create index PROFESORENTRENADOR_FK on PRACTICA (
   IDDOCENTEFK ASC
);

/*==============================================================*/
/* Index: ESPACIOASIGNADO_FK                                    */
/*==============================================================*/
create index ESPACIOASIGNADO_FK on PRACTICA (
   IDESPACIOFK ASC
);

/*==============================================================*/
/* Table: ROL                                                   */
/*==============================================================*/
create table ROL 
(
   IDROL                VARCHAR2(10)         not null,
   DESCROL              VARCHAR2(30)         not null,
   constraint PK_ROL primary key (IDROL)
);

/*==============================================================*/
/* Table: SEDE                                                  */
/*==============================================================*/
create table SEDE 
(
   IDSEDE               VARCHAR2(10)         not null,
   NOMBRESEDE           VARCHAR2(20)         not null,
   DIRECCIONSEDE        VARCHAR2(40)         not null,
   constraint PK_SEDE primary key (IDSEDE)
);

/*==============================================================*/
/* Table: TIPOPRACTICAS                                         */
/*==============================================================*/
create table TIPOPRACTICAS 
(
   IDTIPOPRACTICA       NUMBER(2)            not null,
   DESCPRACTCA          VARCHAR2(15)         not null,
   constraint PK_TIPOPRACTICAS primary key (IDTIPOPRACTICA)
);

alter table ASISTENCIA
   add constraint FK_ASISTENC_ESTUDIANT_ESTUDIAN foreign key (IDESTUDIANTEFK)
      references ESTUDIANTE (IDESTUDIANTE);

alter table ASISTENCIA
   add constraint FK_ASISTENC_PRACTICA_PRACTICA foreign key (IDESPACIOFK, IDPRACTICAFK)
      references PRACTICA (IDESPACIOFK, IDPRACTICA);

alter table DEPORTE
   add constraint FK_DEPORTE_MATERIALE_MATERIAL foreign key (IDMATERIALFK)
      references MATERIAL (IDMATERIAL);

alter table ESPACIO
   add constraint FK_ESPACIO_HORARIOS_HORARIO foreign key (IDHORARIOFK)
      references HORARIO (IDHORARIO);

alter table ESPACIO
   add constraint FK_ESPACIO_SEDEESPAC_SEDE foreign key (IDSEDEFK)
      references SEDE (IDSEDE);

alter table ESTUDIANTE
   add constraint FK_ESTUDIAN_PASANTE_ROL foreign key (IDROLFK)
      references ROL (IDROL);

alter table HISTORICO
   add constraint FK_HISTORIC_HISTORICO_PRACTICA foreign key (IDESPACIOFK, IDPRACTICAFK)
      references PRACTICA (IDESPACIOFK, IDPRACTICA);

alter table HORARIO
   add constraint FK_HORARIO_DIAS_DIA foreign key (IDDIAFK)
      references DIA (IDDIA);

alter table HORARIO
   add constraint FK_HORARIO_HORAS_HORA foreign key (IDHORAFK)
      references HORA (IDHORA);

alter table INSTRUCTOR
   add constraint FK_INSTRUCT_PROFESORO_SEDE foreign key (IDSEDEFK)
      references SEDE (IDSEDE);

alter table INSTRUCTOR
   add constraint FK_INSTRUCT_TIPOINSTR_ROL foreign key (IDROLFK)
      references ROL (IDROL);

alter table MATERIAL
   add constraint FK_MATERIAL_ESTADOMAT_ESTADO foreign key (IDESTADOFK)
      references ESTADO (IDESTADO);

alter table PERSONAL
   add constraint FK_PERSONAL_EMPLEADOS_SEDE foreign key (IDSEDEFK)
      references SEDE (IDSEDE);

alter table PERSONAL
   add constraint FK_PERSONAL_PERSONAL_ROL foreign key (IDROLFK)
      references ROL (IDROL);

alter table PRACTICA
   add constraint FK_PRACTICA_DEPORTEAP_DEPORTE foreign key (IDDEPORTEFK)
      references DEPORTE (IDDEPORTE);

alter table PRACTICA
   add constraint FK_PRACTICA_ESPACIOAS_ESPACIO foreign key (IDESPACIOFK)
      references ESPACIO (IDESPACIO);

alter table PRACTICA
   add constraint FK_PRACTICA_ESTADOPRA_ESTADO foreign key (IDESTADOFK)
      references ESTADO (IDESTADO);

alter table PRACTICA
   add constraint FK_PRACTICA_PASANTEPR_ESTUDIAN foreign key (IDESTUDIANTEFK)
      references ESTUDIANTE (IDESTUDIANTE);

alter table PRACTICA
   add constraint FK_PRACTICA_PROFESORE_INSTRUCT foreign key (IDDOCENTEFK)
      references INSTRUCTOR (IDDOCENTE);

alter table PRACTICA
   add constraint FK_PRACTICA_TIPOPRACT_TIPOPRAC foreign key (IDTIPOPRACTICAFK)
      references TIPOPRACTICAS (IDTIPOPRACTICA);

