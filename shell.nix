{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.uv
    pkgs.python313
    pkgs.python313Packages.ipykernel
    pkgs.ruff
    pkgs.nodejs_22
  ];
}
