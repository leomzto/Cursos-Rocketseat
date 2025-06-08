using System;

namespace HelloWorld;

public class Carro // default de uma classe é internal
{
    public void Ligar() //publico
    {
        Console.WriteLine("Carro LIGADO");
    }

    public void Desligar()
    {
        Console.WriteLine("Carro DESLIGADO");
    }

    private void Teste1() // apenas da classe // default de um metodo é private
    {
        Console.WriteLine("Carro LIGADO");
    }

    internal void Teste2() // mesmo projeto
    {
        Console.WriteLine("TESTE 2");
    }
}
