import axios from 'axios'
import request from './request'


export function getAlgorithm(data){

    return request.get("/behavior")
    .then((res)=>{
        console.log("behavior",res)
        return Promise.resolve(res)
    }).catch((err)=>{
        console.log("behavior fail", )
        return Promise.reject(err)
    })
}