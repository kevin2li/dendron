---
id: ckomqwi87e38a8ff0gk1acr
title: Vue3使用经验总结
desc: ''
updated: 1685156394468
created: 1685108556902
---

## 第三方库
### ant-design-vue
``` bash 
# 安装
pnpm i --save ant-design-vue
```

``` ts 
// main.ts
import { createApp } from "vue";
import Antd from "ant-design-vue";
import App from "./App.vue";
import "ant-design-vue/dist/antd.css";

const app = createApp(App);

app.use(Antd);
app.mount("#app");
```

### ant-design-vue + pinia
``` ts
// main.ts
import { createApp } from "vue";
import { createPinia } from "pinia";
import Antd from "ant-design-vue";
import App from "./App.vue";
import "ant-design-vue/dist/antd.css";

const app = createApp(App);
const pinia = createPinia();
app.use(pinia);
app.use(Antd);
app.mount("#app");
```

### ant-design-vue + pinia + windicss

### ant-design-vue + pinia + windicss + alova



## 代码组织
### 简单小组件
``` ts
<template>
  <div>
    <h1>This is Main</h1>
    <div>count: {{ count }}</div>
    <div><button @click="add">add</button></div>
  </div>
</template>

<script>
import { ref, defineComponent } from "vue";
export default defineComponent({
  components: {},
  props: {},
  setup(props) {
    const msg = ref("Hello, vue3");
    const count = ref(1);
    const add = () => {
      count.value++;
    };
    return {
      add,
      count,
      msg,
    };
  },
});
</script>
```
### 表单
文本框,密码框,数字输入,单选框,多选框,下拉框,checkbox,文件上传等

``` ts
<template>
  <a-form
    :model="formState"
    name="validate_other"
    v-bind="formItemLayout"
    @finishFailed="onFinishFailed"
    @finish="onFinish"
  >
    <a-form-item label="Plain Text">
      <span class="ant-form-text">China</span>
    </a-form-item>
    <a-form-item
      label="Username"
      name="username"
      :rules="[{ required: true, message: 'Please input your username!' }]"
    >
      <a-input v-model:value="formState.username" />
    </a-form-item>

    <a-form-item
      label="Password"
      name="password"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-input-password v-model:value="formState.password" />
    </a-form-item>
    <a-form-item
      name="select"
      label="Select"
      has-feedback
      :rules="[{ required: true, message: 'Please select your country!' }]"
    >
      <a-select v-model:value="formState.select" placeholder="Please select a country">
        <a-select-option value="china">China</a-select-option>
        <a-select-option value="usa">U.S.A</a-select-option>
      </a-select>
    </a-form-item>

    <a-form-item
      name="select-multiple"
      label="Select[multiple]"
      :rules="[{ required: true, message: 'Please select your favourite colors!', type: 'array' }]"
    >
      <a-select
        v-model:value="formState['select-multiple']"
        mode="multiple"
        placeholder="Please select favourite colors"
      >
        <a-select-option value="red">Red</a-select-option>
        <a-select-option value="green">Green</a-select-option>
        <a-select-option value="blue">Blue</a-select-option>
      </a-select>
    </a-form-item>

    <a-form-item label="InputNumber">
      <a-form-item name="input-number" no-style>
        <a-input-number v-model:value="formState['input-number']" :min="1" :max="10" />
      </a-form-item>
      <span class="ant-form-text">machines</span>
    </a-form-item>

    <a-form-item name="switch" label="Switch">
      <a-switch v-model:checked="formState.switch" />
    </a-form-item>

    <a-form-item name="slider" label="Slider">
      <a-slider
        v-model:value="formState.slider"
        :marks="{
          0: 'A',
          20: 'B',
          40: 'C',
          60: 'D',
          80: 'E',
          100: 'F',
        }"
      />
    </a-form-item>

    <a-form-item name="radio-group" label="Radio.Group">
      <a-radio-group v-model:value="formState['radio-group']">
        <a-radio value="a">item 1</a-radio>
        <a-radio value="b">item 2</a-radio>
        <a-radio value="c">item 3</a-radio>
      </a-radio-group>
    </a-form-item>

    <a-form-item
      name="radio-button"
      label="Radio.Button"
      :rules="[{ required: true, message: 'Please pick an item!' }]"
    >
      <a-radio-group v-model:value="formState['radio-button']">
        <a-radio-button value="a">item 1</a-radio-button>
        <a-radio-button value="b">item 2</a-radio-button>
        <a-radio-button value="c">item 3</a-radio-button>
      </a-radio-group>
    </a-form-item>

    <a-form-item name="checkbox-group" label="Checkbox.Group">
      <a-checkbox-group v-model:value="formState['checkbox-group']">
        <a-row>
          <a-col :span="8">
            <a-checkbox value="A" style="line-height: 32px">A</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="B" style="line-height: 32px" disabled>B</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="C" style="line-height: 32px">C</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="D" style="line-height: 32px">D</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="E" style="line-height: 32px">E</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="F" style="line-height: 32px">F</a-checkbox>
          </a-col>
        </a-row>
      </a-checkbox-group>
    </a-form-item>

    <a-form-item name="rate" label="Rate">
      <a-rate v-model:value="formState.rate" allow-half />
    </a-form-item>

    <a-form-item name="upload" label="Upload" extra="longgggggggggggggggggggggggggggggggggg">
      <a-upload
        v-model:fileList="formState.upload"
        name="logo"
        action="/upload.do"
        list-type="picture"
      >
        <a-button>
          <template #icon><UploadOutlined /></template>
          Click to upload
        </a-button>
      </a-upload>
    </a-form-item>

    <a-form-item label="Dragger">
      <a-form-item name="dragger" no-style>
        <a-upload-dragger v-model:fileList="formState.dragger" name="files" action="/upload.do">
          <p class="ant-upload-drag-icon">
            <InboxOutlined />
          </p>
          <p class="ant-upload-text">Click or drag file to this area to upload</p>
          <p class="ant-upload-hint">Support for a single or bulk upload.</p>
        </a-upload-dragger>
      </a-form-item>
    </a-form-item>

    <a-form-item :wrapper-col="{ span: 12, offset: 6 }">
      <a-button type="primary" html-type="submit">Submit</a-button>
    </a-form-item>
  </a-form>
</template>
<script lang="ts">
import { defineComponent, reactive } from 'vue';
import { UploadOutlined, InboxOutlined } from '@ant-design/icons-vue';

export default defineComponent({
  components: {
    UploadOutlined,
    InboxOutlined,
  },
  setup() {
    const formItemLayout = {
      labelCol: { span: 6 },
      wrapperCol: { span: 14 },
    };

    const formState = reactive<Record<string, any>>({
      'username': "",
      'password': "",
      'input-number': 3,
      'checkbox-group': ['A', 'B'],
      rate: 3.5,
    });
    const onFinish = (values: any) => {
      console.log('Success:', values);
    };

    const onFinishFailed = (errorInfo: any) => {
      console.log('Failed:', errorInfo);
    };
    return {
      formState,
      onFinish,
      onFinishFailed,
      formItemLayout,
    };
  },
});
</script>
```
效果:

![](https://minio.kevin2li.top/image-bed/blog/20230527100419.png)

### 表格

主要是定义好column和data.

``` ts
<template>
  <a-table :columns="columns" :data-source="data">
    <template #headerCell="{ column }">
      <template v-if="column.key === 'name'">
        <span>
          <smile-outlined />
          Name
        </span>
      </template>
    </template>

    <template #bodyCell="{ column, record }">
      <template v-if="column.key === 'name'">
        <a>
          {{ record.name }}
        </a>
      </template>
      <template v-else-if="column.key === 'tags'">
        <span>
          <a-tag
            v-for="tag in record.tags"
            :key="tag"
            :color="tag === 'loser' ? 'volcano' : tag.length > 5 ? 'geekblue' : 'green'"
          >
            {{ tag.toUpperCase() }}
          </a-tag>
        </span>
      </template>
      <template v-else-if="column.key === 'action'">
        <span>
          <a>Invite 一 {{ record.name }}</a>
          <a-divider type="vertical" />
          <a>Delete</a>
          <a-divider type="vertical" />
          <a class="ant-dropdown-link">
            More actions
            <down-outlined />
          </a>
        </span>
      </template>
    </template>
  </a-table>
</template>
<script lang="ts">
import { SmileOutlined, DownOutlined } from '@ant-design/icons-vue';
import { defineComponent } from 'vue';
const columns = [
  {
    name: 'Name',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: 'Age',
    dataIndex: 'age',
    key: 'age',
  },
  {
    title: 'Address',
    dataIndex: 'address',
    key: 'address',
  },
  {
    title: 'Tags',
    key: 'tags',
    dataIndex: 'tags',
  },
  {
    title: 'Action',
    key: 'action',
  },
];

const data = [
  {
    key: '1',
    name: 'John Brown',
    age: 32,
    address: 'New York No. 1 Lake Park',
    tags: ['nice', 'developer'],
  },
  {
    key: '2',
    name: 'Jim Green',
    age: 42,
    address: 'London No. 1 Lake Park',
    tags: ['loser'],
  },
  {
    key: '3',
    name: 'Joe Black',
    age: 32,
    address: 'Sidney No. 1 Lake Park',
    tags: ['cool', 'teacher'],
  },
];

export default defineComponent({
  components: {
    SmileOutlined,
    DownOutlined,
  },
  setup() {
    return {
      data,
      columns,
    };
  },
});
</script>
```

![](https://minio.kevin2li.top/image-bed/blog/20230526223848.png)

### 画图
- G2Plot
``` bash
# 安装 
npm install @antv/g2plot
```
要点:
1. 导入onMounted
2. 画图代码放在`onMounted`里


示例：
``` ts 
<template>
  <div>
    <h1>Chart Demo</h1>
    <div style="margin: 30px;" id="container1"></div>
    <div style="margin: 30px;" id="container2"></div>
    <div style="margin: 30px;" id="container3"></div>
  </div>
</template>

<script>
import { ref, defineComponent, onMounted } from "vue";
import { Line, Bar, Pie } from "@antv/g2plot";

export default defineComponent({
  components: {},
  props: {},
  setup(props) {
    onMounted(() => {
      // 折线图
      const data = [
        { year: "1991", value: 3 },
        { year: "1992", value: 4 },
        { year: "1993", value: 3.5 },
        { year: "1994", value: 5 },
        { year: "1995", value: 4.9 },
        { year: "1996", value: 6 },
        { year: "1997", value: 7 },
        { year: "1998", value: 9 },
        { year: "1999", value: 13 },
      ];
      const line = new Line("container1", {
        data: data,
        xField: "year",
        yField: "value",
      });

      line.render();

      // 直方图
      const data2 = [
        { year: "1951 年", value: 38 },
        { year: "1952 年", value: 52 },
        { year: "1956 年", value: 61 },
        { year: "1957 年", value: 145 },
        { year: "1958 年", value: 48 },
      ];

      const bar = new Bar("container2", {
        data: data2,
        xField: "value",
        yField: "year",
        seriesField: "year",
        legend: {
          position: "top-left",
        },
      });

      bar.render();

      // 饼图
      const data3 = [
        { type: "分类一", value: 27 },
        { type: "分类二", value: 25 },
        { type: "分类三", value: 18 },
        { type: "分类四", value: 15 },
        { type: "分类五", value: 10 },
        { type: "其他", value: 5 },
      ];

      const piePlot = new Pie("container3", {
        appendPadding: 10,
        data: data3,
        angleField: "value",
        colorField: "type",
        radius: 0.9,
        label: {
          type: "inner",
          offset: "-30%",
          content: ({ percent }) => `${(percent * 100).toFixed(0)}%`,
          style: {
            fontSize: 14,
            textAlign: "center",
          },
        },
        interactions: [{ type: "element-active" }],
      });

      piePlot.render();
    });
    return {};
  },
});
</script>

```

![](https://minio.kevin2li.top/image-bed/blog/2023-05-26_223043.png)

### 状态存储
- Pinia
> 参考:https://juejin.cn/post/7078281612013764616

``` bash 
# 安装(vue 3.3.0以上,不然会报错)
npm install pinia
```
  - `main.ts`挂载pinia: 见`第三方库`部分

  - 创建store:
``` ts
// src/store/demo.ts
import { defineStore } from "pinia";

interface User {
  username: string;
  gender: string;
  age: number;
}

export const demoStore = defineStore("demo", {
    state: (): User =>({
        username: "kevin",
        gender: "male",
        age: 25,
    }),
    getters: {

    },
    actions: {
        resetState(){
            this.username = "";
            this.gender = "male";
            this.age = 0;
        }
    }
})
```

  - 使用store:
``` ts
// src/components/demo.vue
<template>
  <div>username: {{ store.username }}</div>
  <div>gender: {{ store.gender }}</div>
  <div>age: {{ store.age }}</div>
</template>

<script>
import { ref, defineComponent } from "vue";
import {demoStore} from "../store/demo.ts"

export default defineComponent({
  components: {},
  props: {},
  setup(props) {
    const store = demoStore();
    return { store };
  },
});
</script>
```
### 网络请求
- Alova
参考: https://alova.js.org/zh-CN/
``` bash 
# 安装
npm install alova
```

``` ts
<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="error">{{ error.message }}</div>
  <span v-else>responseData: {{ data }}</span>
</template>

<script setup>
  import { createAlova, useRequest } from 'alova';
  import GlobalFetch from 'alova/GlobalFetch';
  import VueHook from 'alova/vue';

  // 1. 创建alova实例
  const alovaInstance = createAlova({
    // VueHook用于创建ref状态，包括请求状态loading、响应数据data、请求错误对象error等
    statesHook: VueHook,

    // 请求适配器，推荐使用fetch请求适配器
    requestAdapter: GlobalFetch(),

    // 全局的响应拦截器
    responded: response => response.json()
  });

  // 2. 使用alova实例创建method并传给useRequest即可发送请求
  const { loading, data, error } = useRequest(
    alovaInstance.Get('http://localhost:7000', {
      params: {
        // id: 1
      }
    })
  );
</script> 
```

### 表格数据导入与导出
- xlsx


## 组件概念

### `ref`、`reactive`、`toRaw`、`toRefs`、`unref`作用


在Vue 3中，toRaw和toRefs都是用于将响应式对象转换为普通对象的函数，但它们的作用不同。

- `ref`是一个用于创建响应式数据的函数，它可以将一个普通的JavaScript值转换为响应式数据。ref函数返回一个包含了原始值的响应式对象，可以通过.value访问原始值，修改原始值时会触发响应式更新。需要注意的是，ref函数只能用于创建包含一个值的响应式对象。如果需要创建包含多个值的响应式对象，可以使用reactive函数。另外，ref函数也可以用于包装普通的对象或者数组，从而实现对对象或者数组的某个属性或者元素进行响应式更新。

``` ts
const message = ref('Hello, Vue 3!')

// 修改ref对象的值
message.value = 'Hello, World!' 
```

- `reactive`是一个用于创建响应式对象的函数，它可以将一个普通的JavaScript对象转换为响应式对象。reactive函数返回一个代理对象，可以通过该代理对象的属性访问原始对象的属性，对代理对象的属性进行修改时会触发响应式更新。

使用reactive函数创建的响应式对象可以用于模板中的数据绑定，也可以在JavaScript代码中进行操作。在模板中，会自动对响应式数据进行解包，所以可以直接使用响应式对象的属性。在JavaScript代码中，可以直接访问响应式对象的属性，而不需要使用.value来访问原始值。

``` ts
const user = reactive({
    name: 'Tom',
    age: 18
})

// 修改响应式对象的值
user.name = 'Jerry' 
```
- `toRaw`函数用于将一个响应式对象转换为原始对象，即去除响应式特性的对象。这个函数返回的对象不再具有响应式特性，因此在修改它时不会触发响应式更新。这个函数通常用于开发插件或者调试工具时，或者在需要对响应式数据进行深拷贝或者序列化时使用。

``` ts
const user = reactive({
    name: 'Tom',
    age: 18
})

// 将响应式对象转换为原始对象
const userObject = toRaw(user)
```
- `toRefs`函数用于将一个响应式对象的所有属性都转换为普通的属性，并且保留属性的响应式特性。这个函数返回的是一个包含了原始对象中所有属性的响应式对象，其中每个属性都是一个ref对象，可以通过.value访问属性的值。这个函数通常用于需要将响应式对象的属性传递给子组件时使用。
``` ts
const user = reactive({
    name: 'Tom',
    age: 18
})

// 将响应式对象的所有属性都转换为ref对象
const userRefs = toRefs(user) 
```

- `unref`函数的作用是为了简化代码，避免在处理数据时需要判断数据类型。因为在Vue 3中，模板中的数据绑定会自动对响应式数据进行解包，但在JavaScript代码中，需要手动解包响应式数据或者ref对象，才能获取原始值。使用unref函数可以避免这个问题，无论传入的参数是响应式数据还是ref对象，都可以直接获取原始值，避免了代码中的冗余判断。

``` ts
const message = ref('Hello, Vue 3!')
// 使用unref函数获取ref对象的原始值
const messageText = unref(message) 
```