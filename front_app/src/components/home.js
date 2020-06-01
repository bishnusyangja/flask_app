import React from 'react';
import {useState, useEffect} from 'react';
import { Button, Radio, Table, Pagination, notification, Upload, Form} from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import Request from '../api'

 const HomePage = () => {

    const pagination = {pageSize: 10, page: 1};

    const [state, setState] = useState({
        data:null, start: false, count: 0
    });

    const [file_data, setFile] = useState({file: null});

    useEffect(() => {
        console.log("welcome");
        getReport(pagination.page, pagination.pageSize);
      }, []);

    const notify_success = () => {
      notification.open({
        message: 'Upload Successful !!',
        description:
          'The file is successfully uploaded. Report will display after few minutes.',
        onClick: () => {
          console.log('Notification Clicked!');
        },
      });
    };

    const fileUploadChange = (file, fileList) => {
        setFile({file: file.file});
    }


    const getReport = (page, pageSize) => {
        Request().get('/report/', {page: page, page_size: pageSize})
          .then((response) => {
            setState({data: response.data.results, count: response.data.count, start: true});
          })
          .catch((error) => {
            console.log("error at report", error)
          })
          .finally(() => {
            console.log('finally block at report')
        });
    }

    const uploadFile = () => {
        let formData = new FormData();
        console.log(file_data.file);
        formData.append("file", file_data.file);
        Request().post('/upload-file/', formData)
          .then((response) => {
            notify_success();
          })
          .catch((error) => {
            console.log("error in quiz submission")
          })
          .finally(() => {
            console.log('finally block at quiz')
        });
    }


    const columns = [
      {
        title: 'SN',
        dataIndex: '',
        key: 'sn',
        render: (text, record, index) =>  (pagination.page - 1) * pagination.pageSize + index+1,
      },
      {
        title: 'Name',
        dataIndex: 'user_name',
        key: 'name',
      },

      {
        title: 'Keyword',
        dataIndex: 'keyword',
        key: 'keyword',
      },

      {
        title: 'No of Results',
        dataIndex: 'results',
        key: 'result',
      },
   ]

    const onPageChange = (page, pageSize) => {
        console.log("on page change");
        getReport(page, pageSize);
    }

    return (<>
        <div style={{align: 'center', margin: '100px'}}>
            <Form onFinish={uploadFile}>
                <Form.Item> <Upload  beforeUpload={() => false} onChange={fileUploadChange}>
                    <Button>
                      <UploadOutlined
                        /> Select File
                    </Button>
                  </Upload>
                </Form.Item>
                <Form.Item>  <Button type="primary" htmlType="submit">  Upload </Button> </Form.Item>
            </Form>
        </div>

        <div style={{align: 'center', margin: '100px'}}>
            <h2> Search Report</h2>
                {state.data && <Table dataSource={state.data} columns={columns} pagination={false}/>}
                <Pagination defaultCurrent={1}
                          pageSize={pagination.pageSize}
                          total={state.count}
                          onChange={onPageChange}/>
        </div>
    </>);


  }

export default HomePage