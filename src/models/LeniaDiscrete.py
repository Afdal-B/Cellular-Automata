'''function pre_calculate_kernel(beta, dx)
  @radius = get_polar_radius_matrix(SIZE_X, SIZE_Y) * dx
  @Br = size(beta) * @radius
  @kernel_shell = beta[floor(@Br)] * kernel_core(@Br % 1)
  @kernel = @kernel_shell / sum(@kernel_shell)
  @kernel_FFT = FFT_2D(@kernel)
  return @kernel, @kernel_FFT
end'''
import numpy as np
class DiscreteLenia:
    def __init__(self,SIZE_X, SIZE_Y):
        self.SIZE_X = SIZE_X
        self.SIZE_Y = SIZE_Y

    def pre_calculate_kernel(self, beta, dx):
       radius = self.get_polar_radius_matrix(self.SIZE_X,self.SIZE_Y)*dx
       Br = beta.size[0] * radius
       kernel_shell = beta[np.floor(Br)] * self.kernel_core(Br % 1)
       kernel = kernel_shell /np.sum(kernel_shell)
       kernel_FFT = np.fft.fft2(kernel)
       return kernel, kernel_FFT
    
    def get_polar_radius_matrix(self, SIZE_X, SIZE_Y):
        x = np.arange(-SIZE_X/2, SIZE_X/2)
        y = np.arange(-SIZE_Y/2, SIZE_Y/2)
        xx, yy = np.meshgrid(x, y)
        return np.sqrt(xx**2 + yy**2)
    
    def kernel_core(self, x):
        pass


    
    