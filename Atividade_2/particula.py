class Particula:
    def __init__(self, x, y, vx, vy, massa, limites=None, k_arrasto=0.0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.massa = massa
        self.k_arrasto = k_arrasto  # Coeficiente de arrasto
        self.t = 0.0

        # Limites do espaço (x_min, x_max, y_min, y_max)
        self.limites = limites  # Ex: (0, 20, 0, 10)

        # Históricos
        self.l_x = [x]
        self.l_y = [y]
        self.l_vx = [vx]
        self.l_vy = [vy]
        self.l_t = [self.t]

    def newton(self, fx, fy, dt):
        # Força de arrasto 
        fx_total = fx - self.k_arrasto * self.vx
        fy_total = fy - self.k_arrasto * self.vy

        # Aceleração
        ax = fx_total / self.massa
        ay = fy_total / self.massa

        # Atualiza velocidade
        self.vx += ax * dt
        self.vy += ay * dt

        # Atualiza posição
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Rebote nas paredes se houver limites
        if self.limites:
            x_min, x_max, y_min, y_max = self.limites

            if self.x < x_min:
                self.x = x_min
                self.vx *= -1

            elif self.x > x_max:
                self.x = x_max
                self.vx *= -1

            if self.y < y_min:
                self.y = y_min
                self.vy *= -1

            elif self.y > y_max:
                self.y = y_max
                self.vy *= -1

        # Atualiza tempo
        self.t += dt

        # Salva histórico
        self.l_x.append(self.x)
        self.l_y.append(self.y)
        self.l_vx.append(self.vx)
        self.l_vy.append(self.vy)
        self.l_t.append(self.t)
