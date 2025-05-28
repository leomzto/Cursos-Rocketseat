using System;
using System.Globalization;

namespace Tipos_Primitivos

{
    public class OutrosTipos
    {
        enum NivelDificuldade
        {
            Facil,
            Normal,
            Dificil
        }

        public static void Main()
        {
            NivelDificuldade dificuldade = NivelDificuldade.Normal;
            Console.WriteLine(dificuldade);

            // var: identifica o tipo
            var nome1 = "Meu Nome";
            string nome2 = "Meu Nome";

            Console.WriteLine($"nome_var: {nome1}");
            Console.WriteLine($"nome_string: {nome2}");

            var data = DateTime.UtcNow;
            Console.WriteLine($"Data atual: {data}");

            // object: nao identifica o tipo, pode considerar como tipo "variavel", pois nao importa
            // object variavel = "nome, numero, qualquer coisa";

            // null:
            int idade = 18; // ou var idade = 18;
            int? idd = null; // caso receba um valor, vai ser tipo inteiro /// nao pode usar var?, pois null nao identifica tipo ///
            bool informou_idade = idd.HasValue; // verifica se tem valor, caso possui valor (has value) = TRUE, se null = FALSE, has no value
            // se enformou idade:
            int idade_informada = idd.Value; // informa o valor informado

            Console.WriteLine($"informou idade: {informou_idade}");
            Console.WriteLine($"idade informada: {idade_informada}");

        }
    }
}
