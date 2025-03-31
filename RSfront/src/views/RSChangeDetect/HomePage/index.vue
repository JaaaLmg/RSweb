<template>  
  <div class="container">  
    <div class="content">  
      <div class="leftlist"></div>
      <div class="maindetect">
        <div class="toptool"> 
          <div class="upload-area before">  
            <h4 class="h4t">前时相遥感影像</h4>  
            <div class="uploadimage">
                <p class="commodity_img">
                      <!-- 上传图片
                        :class="boxdisplay"
                      -->
                      <el-upload
                        :on-success="handleSuccessbefore"
                        list-type="picture-card"
                        :auto-upload="false"
                        :on-change="handleChangesbefore"
                        :before-remove="beforeRemovebefore"
                        :on-preview="handlePictureCardPreviewbefore"
                        :file-list="fileListbefore"
                        multiple
                        limit="1"
                        name="img"
                      >
                        <el-icon class="avatar-uploader-icon">
                          <Plus />
                        </el-icon>
                      </el-upload>
                  </p>

              <el-dialog v-model="dialogVisible">
                <img w-full class="imageshow" :src="dialogImageUrl" alt="Preview Image" />
              </el-dialog>
            </div>
          </div>  
          <div class="upload-area after">  
            <h4 class="h4t">后时相遥感影像</h4>  
            <div class="uploadimage">
                <p class="commodity_img">
                      <!-- 上传图片
                        :class="boxdisplay"
                      -->
                      <el-upload
                        :on-success="handleSuccessafter"
                        list-type="picture-card"
                        :auto-upload="false"
                        :on-change="handleChangesafter"
                        :before-remove="beforeRemoveafter"
                        :on-preview="handlePictureCardPreviewafter"
                        :file-list="fileListafter "
                        multiple
                        limit="1"
                        name="img"
                      >
                        <el-icon class="avatar-uploader-icon">
                          <Plus />
                        </el-icon>
                      </el-upload>
                  </p>

              <el-dialog v-model="dialogVisible">
                <img w-full class="imageshow" :src="dialogImageUrl" alt="Preview Image" />
              </el-dialog>
            </div>
          </div>
          <div class="detectchange">
            <el-button class="uploadimg" @click="uploadimg">开始检测</el-button>
          </div>
        </div> 
        <div class="detectmain">
          <div>
            <el-image class="showimg" :src="srcbefore">

            </el-image>
          </div>
          <div>
            <el-image class="showimg" :src="srcafter">
            </el-image>
          </div>
          <div>
            <el-image  class="showimg" :src="srcdetect">
            </el-image>
          </div>
        </div>
      </div>
      <div class="rightlist"></div>
    </div>  
  </div>  
</template>  
  
<script setup lang="ts">  
 import { ref } from 'vue'
  import { ElMessage } from 'element-plus';
  import { Picture as IconPicture,Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'

  import type { UploadFile } from 'element-plus'
  import axios from 'axios'
  const dialogImageUrl = ref('')
  const dialogVisible = ref(false)
  const disabled = ref(false)
  
  const srcbefore =ref('test')
  
  const srcafter =ref('test')

  const srcdetect =ref('test')
  

  const handleRemove = (file: UploadFile) => {
    file.url = '';
    file=null;
  }
  

  const handlePictureCardPreviewbefore = (file: UploadFile) => {
    dialogImageUrl.value = file.url!
    dialogVisible.value = true
  }
  const handlePictureCardPreviewafter = (file: UploadFile) => {
    dialogImageUrl.value = file.url!
    dialogVisible.value = true
  }


  const boxdisplay = ref("show_box");

  const upload_btn = ref(false);
  const fileListbefore = ref([]);
  const fileListafter = ref([]);

  const handleSuccessbefore = () => {

  };
  const handleSuccessafter = () => {

};

  const handleChangesbefore = img => {
    fileListbefore.value.push(img);
    boxdisplay.value = "hide_box";
    srcbefore.value = "";  
    srcafter.value = "";  
    srcdetect.value = "";  
  };
  const handleChangesafter = img => {
    fileListafter.value.push(img);
    boxdisplay.value = "hide_box";
    srcbefore.value = "";  
    srcafter.value = "";  
    srcdetect.value = ""; 
  };
  import {ElMessageBox} from 'element-plus'
  // 删除
  const beforeRemovebefore = () => {
    const result = new Promise((resolve, reject) => {
      ElMessageBox.confirm("此操作将删除该图片, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          boxdisplay.value = "show_box";
          resolve();
          fileListbefore.value = [];
          upload_btn.value = false;
        })
        .catch(() => {
          reject(false);
        });
    });
    return result;
  };
  const beforeRemoveafter = () => {
    const result = new Promise((resolve, reject) => {
      ElMessageBox.confirm("此操作将删除该图片, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          boxdisplay.value = "show_box";
          resolve();
          fileListafter.value = [];
          upload_btn.value = false;
        })
        .catch(() => {
          reject(false);
        });
    });
    return result;
  };
  const uploadimg = async () => {  
    try {  
        var imga = await uploadimgbefore();  
        var imgb = await uploadimgafter();  
        let formData = new FormData();  
        formData.append("username", "12345");  
        formData.append("imgA", imga);  
        formData.append("imgB", imgb);  
        let url = 'http://127.0.0.1:5000/detectrscd'; //访问后端接口的url  
        let method = 'post';  
        axios({  
            method,  
            url,  
            data: formData,  
            headers: {  
                'Content-Type': 'multipart/form-data' // 确保设置了正确的Content-Type  
            }  
        }).then(res => {  
            srcdetect.value = res.data.url;  
            ElMessage({ message: '变化检测完成', type: 'success' });  
        }).catch(() => {  
            // 处理错误  
        });  
    } catch (error) {  
        console.error("Error uploading images:", error);  
    }  
};  
  
const uploadimgbefore = () => {  
    return new Promise((resolve, reject) => {  
        let formData = new FormData();  
        formData.append("username", "12345");  
        fileListbefore.value.forEach((file, index) => {  
            formData.append("file", file.raw);  
        });  
  
        let url = 'http://127.0.0.1:5000/uploadbefore'; //访问后端接口的url  
        let method = 'post';  
        axios({  
            method,  
            url,  
            data: formData,  
            headers: {  
                'Content-Type': 'multipart/form-data' // 确保设置了正确的Content-Type  
            }  
        }).then(res => {  
            fileListbefore.value = [];  
            upload_btn.value = false;  
            srcbefore.value = res.data.url;  
            ElMessage({ message: '前时相影像上传成功', type: 'success' });  
            resolve(res.data.picpath);  
        }).catch(() => {  
            reject("Failed to upload before image");  
        });  
    });  
};  
  
const uploadimgafter = () => {  
    return new Promise((resolve, reject) => {  
        let formData = new FormData();  
        formData.append("username", "12345");  
        fileListafter.value.forEach((file, index) => {  
            formData.append("file", file.raw);  
        });  
  
        let url = 'http://127.0.0.1:5000/uploadafter'; //访问后端接口的url  
        let method = 'post';  
        axios({  
            method,  
            url,  
            data: formData,  
            headers: {  
                'Content-Type': 'multipart/form-data' // 确保设置了正确的Content-Type  
            }  
        }).then(res => {  
            fileListafter.value = [];  
            upload_btn.value = false;  
            srcafter.value = res.data.url;  
            ElMessage({ message: '后时相影像上传成功', type: 'success' });  
            resolve(res.data.picpath);  
        }).catch(() => {  
            reject("Failed to upload after image");  
        });  
    });  
};
</script>  
  
<style scoped>  
.container {  
  display: grid;  
  grid-template-rows: 100%;
  height: 92vh;
}  
  
  
.content {  
  display: grid;  
  place-items: center;  
  padding: 0em;  
  background-color: #f0f0f0;  
  grid-template-columns: 15% 70% 15%;
}  
  
.upload-area, .result-area {  
  border: 1px dashed #4f4949;
    position: relative;
    padding: 1em;
    height: 69%;
    margin: 1em;
}  
  
.before {  

}  
  
.after {  

}  
  
.result-area {  
  background-color: #aaf;  
}  
  
.result-image {  
  height: 200px;  
  background-color: #eee;  
  display: flex;  
  align-items: center;  
  justify-content: center;  
} 
.leftlist{
  position: relative;
  width: 100%;
  height: 100%;
  background-color: #aac1ff63;
} 
.rightlist{
  position: relative;
  width: 100%;
  height: 100%;
  background-color: #aac1ff63;
}
.maindetect{
  position: relative;
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-rows: 30% 70%;
}
.toptool{
  position: relative;
    width: 100%;
    height: 100%;
    background-color: rgb(201 218 222);
    display: grid;
    grid-template-columns: 40% 40% 20%;
}
.upimg{
  position: relative;
  left: 5%;
  height: 4em;
}
.detectcd{
  position: relative;
  left: 5%;
  height: 4em;
}
.imageshow{
  width: 100%;  
  height: 100%;  
  object-fit: fill; 
}
.detectmain{
  position: relative;
  display: grid;
  grid-template-columns: 33% 33% 33%;
}
.h4t{
  margin: 0;

}
.uploadimg{
  position: relative;
    height: 4em;
    top: 35%;
    left: 10%;
}
.demo-image__error .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 49%;
  box-sizing: border-box;
  vertical-align: top;
}
.demo-image__error .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}
.demo-image__error .el-image {
  padding: 0 5px;
  max-width: 300px;
  max-height: 200px;
  width: 100%;
  height: 200px;
}

.demo-image__error .image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: var(--el-fill-color-light);
  color: var(--el-text-color-secondary);
  font-size: 30px;
}
.demo-image__error .image-slot .el-icon {
  font-size: 30px;
}
.showimg{
  position: relative;
    width: 20vw;
    height: 20vw;
    left: 5%;
    top: 15%;
    background-color:#d7e6f570;
}
</style>