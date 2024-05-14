{
  description = ''A flake for the "Introduction to Quantum Computing" course by Quantum Soar'';

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url  = "github:numtide/flake-utils";
  };

  outputs = { /* self, */ nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in
      with pkgs;
      {
        devShells.default = mkShell {
          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
            pkgs.stdenv.cc.cc
          ];
          buildInputs = [
            python312
            poetry
          ];
          shellHook = ''
            export PS1="(intro-quantum)$PS1"
          '';
        };
      }
    );
}
