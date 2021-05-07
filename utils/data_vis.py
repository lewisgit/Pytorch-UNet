import matplotlib.pyplot as plt
import cv2
import numpy as np
plt.rcParams['figure.figsize'] = [15, 10]
plt.rcParams['figure.dpi'] = 100


def plot_img_and_mask(img, mask, full_mask, use_cv=False):
    classes = mask.shape[2] if len(mask.shape) > 2 else 1
    if use_cv:
        cv2.imshow("Input", np.array(img))
    else:
        fig, ax = plt.subplots(1, classes * 2 + 1)
        ax[0].set_title('Input image')
        ax[0].imshow(img)
    if classes > 1:
        for i in range(classes):
            if use_cv:
                title = f'Output mask (class {i+1})'
                title2 = f'Full mask (class {i+1})'
                #cv2.imshow(title, np.array(mask[:,:,i]))
                cv2.imshow(title2, np.array(full_mask[:,:,i]))
                cv2.waitKey(0)
            else:
                ax[2*i+1].set_title()
                ax[2*i+1].imshow(mask[:, :, i])
                ax[2*i+2].set_title(f'Full mask mask (class {i+1})')
                ax[2*i+2].imshow(full_mask[:, :, i])
    else:
        if use_cv:
            title = f'Output mask'
            title2 = f'Full mask'
            
            #cv2.imshow(title, mask)
            cv2.imshow(title2, full_mask)
            cv2.waitKey(0)
        else:
            ax[1].set_title(f'Output mask')
            ax[1].imshow(mask)
            ax[2].set_title(f'Full mask')
            ax[2].imshow(full_mask)
    if not use_cv:
        plt.xticks([]), plt.yticks([])
        plt.show()
