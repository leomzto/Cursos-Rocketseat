using System.Globalization;
using System.Runtime.ConstrainedExecution;
using System.Text;
using Microsoft.VisualBasic;

namespace Tipos_Primitivos;

public class Primitivos
{
    public static void Main()
    {
        Console.WriteLine("Tipos Numericos: ");
        Numericos();
        Console.WriteLine("\nTipos Booleanos: ");
        Booleanos();
        Console.WriteLine("\nTipos de texto: ");
        Textos();
        Console.WriteLine("\nOperaçoes com textos: ");
        oprTextos();
        Console.WriteLine("\nDatas e Horas: ");
        DatasHoras();
    }

    static void Numericos()
    {
        // byte, ubyte, sbyte

        int int1 = 500; // int
        long int2 = 500; // long int ( more digits)
        uint int3 = 500; // unsigned int (only positive)

        int mil = 1_000;

        float float1 = 3.14f;// less precise
        double float2 = 3.14; // normal
        decimal float3 = 3.14m; // extremely precise

        Console.WriteLine($"int: {int1}");
        Console.WriteLine($"long: {int2}");
        Console.WriteLine($"uint: {int3}");

        Console.WriteLine($"mil: {mil}");

        Console.WriteLine($"float: {float1}");
        Console.WriteLine($"double: {float2}");
        Console.WriteLine($"decimal: {float3}");
    }

    static void Booleanos()
    {
        bool tipo = false;
        bool tipo2 = true;

        Console.WriteLine(tipo);
        Console.WriteLine(tipo2);
    }

    static void Textos()
    {
        char letra = 'a';
        char numero = '1';
        char caractere = '@';
        string palavra = "abcde";
        string texto = "abcde fghi, jklm. nopq!, rstu? vwx... yz$";

        Console.WriteLine($"letra: {letra}");
        Console.WriteLine($"numero: {numero}");
        Console.WriteLine($"caractere: {caractere}");
        Console.WriteLine($"palavra: {palavra}");
        Console.WriteLine($"texto: {texto}");

        //char acessarElemento = <var>[pos];
        Console.WriteLine($"acessar elemento palavra[0]: {palavra[0]}");

        string stringEspacos = "    .     String    .     ";
        // tirar espaços:
        Console.WriteLine($"sem tirar espaços: {stringEspacos}");
        Console.WriteLine($"tirar espaçs inicio/final: {stringEspacos.Trim()}");
        Console.WriteLine($"tirar espaços inicio: {stringEspacos.TrimStart()}");
        Console.WriteLine($"tirar espaços final: {stringEspacos.TrimEnd()}");

        // verificar inicio string:
        string verificar = "www.com.br";
        Console.WriteLine($"a string '{verificar}'inicia com 'www'? {verificar.StartsWith("www")}");
        Console.WriteLine($"a string '{verificar}'inicia com 'https://'? {verificar.StartsWith("https://")}");

        // outrs funçoes:
        // .Replace('antigo', 'novo') ---- (troca um caractere por outro)
        // .Contains("<o que voce quer saber se contem>") ---- (verifica se a string contem os caracteres ou palavra desejada)
        // .Equals("<o que voce quer saber se é igual>") ---- (verifica equidade de strings)
    }

    static void oprTextos() // operaçoes com textos
    {
        string texto1 = "A primeira frase.";
        string texto2 = "Segunda frase";
        string texto1comtexto2 = texto1 + " " + texto2; // " " adiciona um espaço

        string texto3 = "texto 3.";

        Console.WriteLine($@"Junçao de strings: {texto1} + "" "" + {texto2} = {texto1comtexto2}");
        // o \ antes, ignora a funçao original,
        // explo, para imprimir C:\.... deve-se: C:\\...
        // ou usar @ antes de iniciar o "conteudo"

        //stringbuilder
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.Append(texto1comtexto2);
        stringBuilder.Append(texto3);
        string resultado = stringBuilder.ToString();

        Console.WriteLine(resultado);

        // string format:

        string gosta = "O usuario {0} gosta do numero {1}.";

        string resultado_gosta = string.Format(gosta, "USUARIO", "NUMERO");

        Console.WriteLine(resultado_gosta);

    }

    static void DatasHoras()
    {
        DateTime data_presente = DateTime.UtcNow;
        string presente = data_presente.ToString("d 'de' MMMM 'de' yyyy\nHH:mm:ss", new CultureInfo("pt-BR"));

        DateTime data_futuro = data_presente.AddMonths(6);
        string futuro = data_futuro.ToString("d 'de' MMMM 'de' yyyy\nHH:mm:ss", new CultureInfo("pt-BR"));

        Console.WriteLine($"presente: {presente}");

        Console.WriteLine($"futuro (+ 6 meses): {futuro}");
    }

}

