import React, { useEffect } from 'react'
...
...

const { fileProgress, uploadFile } = props
const uploadedFileAmount = size(fileProgress)

useEffect(() => {
  const fileToUpload = toArray(fileProgress).filter(file =>    file.progress === 0)
  uploadFile(fileToUpload)
}, [uploadedFileAmount])
...
...

const mapDispatchToProps = dispatch => ({
  uploadFile: files => dispatch(uploadFile(files)),
})

export default connect(mapStateToProps, mapDispatchToProps)(UploadProgress)
