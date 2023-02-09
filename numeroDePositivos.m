function num = numeroDePositivos(a, b, c, d)
%numeroDePositivos usa un contador para contar! números positivos
contador = 0; % Por defecto, tenemos 0 números positivos.
if (a > 0)
    contador = contador + 1;
end
if (b > 0)
    contador = contador + 1;
end
if (c > 0)
    contador = contador + 1;
end
if (d > 0)
    contador = contador + 1;
end
num = contador;
end