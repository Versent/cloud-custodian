from c7n import handler
def run(event, context):
    handler.dispatch_event(event, context)
