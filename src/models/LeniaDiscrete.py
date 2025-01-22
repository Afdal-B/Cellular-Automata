'''function pre_calculate_kernel(beta, dx)
  @radius = get_polar_radius_matrix(SIZE_X, SIZE_Y) * dx
  @Br = size(beta) * @radius
  @kernel_shell = beta[floor(@Br)] * kernel_core(@Br % 1)
  @kernel = @kernel_shell / sum(@kernel_shell)
  @kernel_FFT = FFT_2D(@kernel)
  return @kernel, @kernel_FFT
end'''
import numpy as np
import matplotlib.pyplot as plt
class DiscreteLenia:
    def __init__(self,SIZE_X, SIZE_Y):
        self.SIZE_X = SIZE_X
        self.SIZE_Y = SIZE_Y

    def pre_calculate_kernel(self, beta, dx):
       radius = self.get_polar_radius_matrix()*dx
       Br = beta.shape[0] * (radius / np.max(radius)) # Normalisation
       kernel_shell = beta[np.floor(Br).astype(int)%beta.shape[0]] * self.kernel_core(Br % 1)
       kernel = kernel_shell /np.sum(kernel_shell)
       #kernel_FFT = np.fft.fft2(kernel)
       return kernel_shell
    
    def get_polar_radius_matrix(self):
        x = np.arange(-self.SIZE_X/2, self.SIZE_X/2)
        y = np.arange(-self.SIZE_Y/2, self.SIZE_Y/2)
        xx, yy = np.meshgrid(x, y)
        return np.sqrt(xx**2 + yy**2)
    
    def kernel_core(self, Br ,function="polynomial",alpha= 4):
        if function == "polynomial":
            return (4*Br*(1-Br))**alpha
        elif function == "exponential":
            return np.exp(alpha - (alpha/(4*Br*(1-Br))))

    """
    function run_automaton(@world, @kernel, @kernel_FFT, mu, sigma, dt)
  if size(@world) is small
    @potential = elementwise_convolution(@kernel, @world)
  else
    @world_FFT = FFT_2D(@world)
    @potential_FFT = elementwise_multiply(@kernel_FFT, @world_FFT)
    @potential = FFT_shift(real_part(inverse_FFT_2D(@potential_FFT)))
  end
  @growth = growth_mapping(@potential, mu, sigma)
  @new_world = clip(@world + dt * @growth, 0, 1)
  return @new_world, @growth, @potential
end
    """


lenia = DiscreteLenia(100,100)
beta = np.array([0.1, 0.2, 0.3])
dx = 1
#polar_radius = lenia.get_polar_radius_matrix() / lenia.get_polar_radius_matrix().max()
#kernel_core = lenia.kernel_core(polar_radius % 1)
kernel = lenia.pre_calculate_kernel(beta, dx)

plt.figure(figsize=(6, 6))
plt.imshow(kernel, cmap="viridis", origin="lower")
plt.colorbar(label="Intensité normalisée")
plt.title("Étape 4 : Noyau final normalisé (K)")
plt.axis("off")
plt.show()


    
    