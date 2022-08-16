# /memallook/app.py
# API used to maintain memory allocations in a buffer

from fastapi import FastAPI
import memalook

app = FastAPI()
m = memalook.Memalook()

@app.get('/')
async def root():
	return "Welcome to Memallook Service!"

# Allows user to create p*N sized buffer
@app.post('/buffer')
async def new_api(size: int, page: int):
	return m.new(size, page)

# Allocates m bytes to buffer, if allowed
@app.post('/buffer/{tag}')
async def alloc_api(byt: int):
	return m.alloc(byt)

# Deallocates block of memory at tag t, if t exists
@app.patch('/buffer/{tag}')
async def dealloc_api(tag: int):
	return m.dealloc(tag)

# Shows current heap
@app.get('/buffer')
async def show_api():
	return m.show()

# Resets already maintained buffer
@app.delete('/buffer')
async def reset_api():
	return m.reset()

# Defragments buffer
@app.delete('/buffer/defrag')
async def defrag_api():
	return m.defrag()
