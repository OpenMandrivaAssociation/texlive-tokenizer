Name:		texlive-tokenizer
Version:	15878
Release:	2
Summary:	A tokenizer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tokenizer
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tokenizer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tokenizer.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A tokenizer for LaTeX. \GetTokens{Target1}{Target2}{Source}
Splits Source into two tokens at the first encounter of a
comma. The first token is saved in a newly created command with
the name passed as Target1 and the second token likewise. A
package option 'trim' causes leading and trailing space to be
removed from each token; with this option, the \TrimSpaces
command is defined, which removes leading and trailing spaces
from its argument.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tokenizer/tokenizer.sty
%doc %{_texmfdistdir}/doc/latex/tokenizer/tokenizer.pdf
%doc %{_texmfdistdir}/doc/latex/tokenizer/tokenizer.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
