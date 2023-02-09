function area = calculaAreaTriangulo(lado)
    if (lado > 0)
        area = lado*lado;
    else
        disp("el lado debe ser positivo");
        area = 0;
    end
end