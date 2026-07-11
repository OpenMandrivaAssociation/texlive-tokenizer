%global tl_name tokenizer
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0
Release:	%{tl_revision}.1
Summary:	A tokenizer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tokenizer
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tokenizer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tokenizer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A tokenizer for LaTeX. \GetTokens{Target1}{Target2}{Source} splits
source into two tokens at the first encounter of a comma. The first
token is saved in a newly created command with the name passed as
<Target1> and the second token likewise. A package option 'trim' causes
leading and trailing space to be removed from each token; with this
option, the \TrimSpaces command is defined, which removes leading and
trailing spaces from its argument.

