import axios from "axios";

const service = axios.create({
    baseURL:"http://localhost:8000/",
    timeout:5000
})

//请求拦截器
service.interceptors.request.use(
    config=>{
        // config.headers["lanjie"] = "yy"
        // console.log("request")
        config.headers['Authorization'] = 'Bearer' + ' ' + localStorage.getItem('token')
        return config
    },
    error => {
        console.log("Request error",error)
        return Promise.reject(error)
    }
)

service.interceptors.response.use(
    response => {
        console.log("response",response)
        if (response.status===200 && response.data.code===0){
            return Promise.resolve(response.data.data)
        }else{
            return Promise.reject(response.data)
        }
    },
    err =>{
        console.log("Response Error:",err)
        return Promise.reject(err)
    }
)
export default service