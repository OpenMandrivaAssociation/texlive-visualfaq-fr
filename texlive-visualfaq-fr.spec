Name:		texlive-visualfaq-fr
Version:	67718
Release:	1
Summary:	FAQ LaTeX visuelle francophone
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/visualfaq-fr
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/visualfaq-fr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/visualfaq-fr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
(French version below.) The Visual LaTeX FAQ is an innovative
new search interface on LaTeX Frequently Asked Questions. This
version is a French translation, offering links to the
French-speaking LaTeX FAQ. Vous avez du mal a trouver la
reponse a une question sur LaTeX ou meme a trouver les mots
pour exprimer votre question? La FAQ LaTeX visuelle est une
interface de recherche innovante qui presente plus d'une
centaine d'exemples de mises en forme de documents frequemment
demandees. Il suffit de cliquer sur l'hyperlien qui correspond
a ce que vous souhaitez faire - ou ne pas faire - et la FAQ
LaTeX visuelle enverra votre navigateur web a la page
correspondante de la FAQ LaTeX francophone.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/visualfaq-fr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
