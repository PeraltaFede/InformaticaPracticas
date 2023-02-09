function resultado = f2(x, y, z, t)
producto = x * y * z* t;
cant_positivos = numeroDePositivos(x,y ,z , t);
if (cant_positivos < 4)
    resultado = producto + cant_positivos;
else
    resultado = producto;
end
end