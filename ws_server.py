from autobahn.twisted.websocket import WebSocketServerProtocol, \
                                       WebSocketServerFactory


class LeaderboardProtocol(WebSocketServerProtocol):

    def onOpen(self):
        print 'Connection opened'

    def onConnect(self, request):
        self.factory.protocols.append(self)
        print 'Connection Success'

    def onMessage(self, payload, isBinary):
        print 'Message recieved %s' % payload
        for protocol in self.factory.protocols:
            protocol.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        print 'Connection Close'


if __name__ == '__main__':
    import sys
    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
    factory.clients = []
    factory.protocol = LeaderboardProtocol

    reactor.listenTCP(9000, factory)
    reactor.run()
