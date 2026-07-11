%global tl_name visualfaq-fr
%global tl_revision 71053

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	FAQ LaTeX visuelle francophone
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/visualfaq-fr
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/visualfaq-fr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/visualfaq-fr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
(French version below.) The Visual LaTeX FAQ is an innovative new search
interface on LaTeX Frequently Asked Questions. This version is a French
translation, offering links to the French-speaking LaTeX FAQ. Vous avez
du mal a trouver la reponse a une question sur LaTeX ou meme a trouver
les mots pour exprimer votre question? La FAQ LaTeX visuelle est une
interface de recherche innovante qui presente plus d'une centaine
d'exemples de mises en forme de documents frequemment demandees. Il
suffit de cliquer sur l'hyperlien qui correspond a ce que vous souhaitez
faire - ou ne pas faire - et la FAQ LaTeX visuelle enverra votre
navigateur web a la page correspondante de la FAQ LaTeX francophone.

