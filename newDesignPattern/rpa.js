class RecursivePathAcessor {
    constructor(obj) {
        this.obj = obj
    }

    get(path) {
        return this.#recursiveGet(this.obj, path.split('.')) 
    }

    set(path, value) {
        return this.#recursiveSet(this.obj, path.split('.'), value)
    }

    has(path) {
        return this.#recursiveHas(this.obj, path.split('.'))
    }

    delete(path) {
        return this.#recursiveDelete(this.obj, path.split('.'))
    }

    #recursiveGet(obj, pathArr) {
        console.log("recusiveGet", obj, pathArr)
        if(!obj || typeof obj !== 'object') {
            return undefined;
        }

        const [head, ...tail] = pathArr;
        if(!head) {
            return obj
        }

        return this.#recursiveGet(obj[head], tail)
    }

    #recursiveSet(obj, pathArr, value) {
        const [head, ...tail] = pathArr;
        if(!head) {
            return
        }

        if(tail.length === 0) {
            obj[head] = value
            return 
        }

        if(!obj[head]) obj[head] = {}
        this.#recursiveSet(obj[head], tail, value)
    }

    #recursiveHas(obj, pathArr) {
        if(!obj || typeof obj !== 'object') {
            return false
        }

        const [head, ...tail] = pathArr;
        if(!head) {
            return true
        }

        return this.#recursiveHas(obj[head], tail)
    }

    #recursiveDelete(obj, pathArr) {
        if(!obj || typeof obj !== 'object') {
            return false
        }

        const [head, ...tail] = pathArr;
        if(tail.length === 0) {
            return delete obj[head]
        }

        return this.#recursiveDelete(obj[head], tail)
    }
}

const data = {
    usuario: {
        perfil: {
            nome: "Pedro",
            preferencias: {
                tema: "escuro",
                idioma: "pt"
            }
        }
    }
}

const rpa = new RecursivePathAcessor(data)

const user = data.usuario.perfil.nome

console.log(rpa.get('usuario.perfil.preferencias.tema'))

// rpa.set('usuario.perfil.idade', 25)
// console.log(data.usuario.perfil.idade)

// console.log(rpa.has('usuario.perfil.nome'))

// rpa.delete('usuario.perfil.preferencias.tema')
// console.log(rpa.get('usuario.perfil.preferencias.tema'))

