/*
Mini Avaliação II
Vitor Frango 
PEDRA / PAPEL / TESOURA

Pedir ao utilizador 1 que insira uma opção: “Pedra”, “Papel” ou Tesoura2.
Pedir ao utilizador 2 que insira uma opção: “Pedra”, “Papel” ou Tesoura3.
Mostrar o resultado do jogo:

Ex:PedraPapelResultado => Ganhou o Jogador 2
Ex:PedraPedraResultado => Empate
Ex:TesouraPapelResultado => Ganhou o Jogador 1
*/


#include <iostream>

int main () {

    // define variaeis do tipo string para introdução de texto 
    std::string player1, player2;

    // pedido de introdução de dados aos dois jogadores e grava nas variaveis 
    std::cout << "Jogador 1: Insira uma opção: Pedra, Papel ou Tesoura" << std::endl;
    std::cin >> player1;

    std::cout << "Jogador 2: Insira uma opção: Pedra, Papel ou Tesoura" << std::endl;
    std::cin >> player2; 

    
    // ciclo que testa as diferentes entradas e imprime resultado
    if ((player1 == "tesoura") && (player2 == "papel" ) || (player1 == "pedra") && (player2 == "tesoura" ) || (player1 == "papel") && (player2 == "pedra" )){
        std::cout << "Ganhou o joagaor 1" << std::endl; 
    }
    else if ((player2 == "tesoura") && (player1 == "papel" ) || (player2 == "pedra") && (player1 == "tesoura" ) || (player2 == "papel") && (player1 == "pedra" )){
        std::cout << "Ganhou o joagaor 2" << std::endl; 
    }

    // caso não preencha as permissas antariores é pq empataram 
    else {
        std::cout << " Os jogadores empataram " << std::endl;
    
    }
    
    return 0;
}