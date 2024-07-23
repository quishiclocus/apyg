### This works for making a nix-shell.
#{ pkgs ? import <nixpkgs> {} }:
#pkgs.mkShell {
#  # buildInputs is for dependencies you'd need "at run time",
#  # were you to to use nix-build not nix-shell and build whatever you were working on
#  buildInputs = [
#    (import ./apyg.nix)
#  ];
#}
###

(import (
  let
    lock = builtins.fromJSON (builtins.readFile ./flake.lock);
  in fetchTarball {
    url = "https://github.com/edolstra/flake-compat/archive/${lock.nodes.flake-compat.locked.rev}.tar.gz";
    sha256 = lock.nodes.flake-compat.locked.narHash; }
) {
  src =  ./.;
}).defaultNix
