
import processfile
import globleVar
import vggnet
import train
import torch


if __name__ == '__main__':
    # copy train data from source path to source train path
    # processfile.cpFIle(globleVar.SOURCE_PATH,globleVar.SOURCE_TRAIN_PATH,globleVar.TRAIN_CONFIG_FILE,'wav')
    # copy test data from source path to source test path
    # processfile.cpFIle(globleVar.SOURCE_PATH,globleVar.SOURCE_TEST_PATH,globleVar.TEST_CONFIG_FILE,'wav')
    # copy evaluation data from source path to source evaluate path
    # processfile.cpFIle(globleVar.SOURCE_PATH, globleVar.SOURCE_EVALUATION_PATH, globleVar.EVALUATION_CONFIG_FILE,'wav')

    # copy train data from source train path to train path
    # processfile.cpFIle(globleVar.SOURCE_TRAIN_PATH,globleVar.TRAIN_PATH,globleVar.TRAIN_CONFIG_FILE,'jpg')
    # copy evaluate data from source evaluate path to evaluate path
    # processfile.cpFIle(globleVar.SOURCE_EVALUATION_PATH,globleVar.EVALUATION_PATH,globleVar.EVALUATION_CONFIG_FILE,'jpg')

    # Print model
    # block_demo = VGG_Net.vgg_block(3, 64, 128)
    # print(block_demo)

    # 首先定义输入为 (1, 64, 300, 300)
    # input_demo = VGG_Net.Variable(torch.zeros(1, 64, 300, 300))
    # output_demo = block_demo(input_demo)
    # print(output_demo.shape)
    #
    # vgg_net = VGG_Net.vgg_stack((1, 1, 2, 2, 2), ((3, 64), (64, 128), (128, 256), (256, 512), (512, 512)))
    # print(vgg_net)
    #
    # test_x = VGG_Net.Variable(torch.zeros(1, 3, 256, 256))
    # test_y = vgg_net(test_x)
    # print(test_y.shape)

    train.train()
    # train.predict()




