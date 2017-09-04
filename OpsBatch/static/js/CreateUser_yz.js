$(document).ready(function() {
    $('#create_form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            create_username: {
                message: '用户名无效',
                validators: {
                    notEmpty: {
                        message: '用户名不能为空'
                    },
                    stringLength: {
                        min: 3,
                        max: 30,
                        message: '用户名的长度在3和30之间'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9_]+$/,
                        message: '用户名只能由字母、数字和下划线'
                    }
                }
            },
           create_password: {
                validators: {
                    notEmpty: {
                        message: '密码必须填写,不能为空'
                    },
                    identical: {
                        field: 'create_repassword',
                        message: '两次密码不相同'
                    },
                    different: {
                        field: 'create_username',
                        message: '密码不能和用户名一样'
                    }
                }
            },
            create_repassword: {
                validators: {
                    notEmpty: {
                        message: '密码必须填写,不能为空'
                    },
                    identical: {
                        field: 'create_password',
                        message: '两次密码不相同'
                    },
                    different: {
                        field: 'create_username',
                        message: '密码不能和用户名一样'
                    }
                }
            },
            create_ms: {
                validators: {
                    notEmpty: {
                      message:'请填写用户描述信息！'
                    }
                }
            }
        }
    });
});
